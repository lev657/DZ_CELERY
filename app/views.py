from flask import request, jsonify
from flask.views import MethodView
from app import app
from app.validator import validate
from app.models import Ad, User
from app.schema import USER_CREATE, AD_CREATE
from app.tasks import send_async_email


# реализованы методы создания/удаления/редактирования объявления
# POST метод создаёт объявление, GET - получает объявление, DELETE - удаляет объявление.


# метод API, рассылающий email всем пользователям
# POST запрос создает задачу на рассылку, отправляет в Celery и возвращает task_id
# GET с параметром task_id в uri возвращает статус задачи.
# добавлен фильтр, чтобы сообщения отправлялись не всем пользователям,
# а только соответствующим определенным параметрам, передаваемым в POST запросе.
# в данном примере фильтрация по имени или части имени пользователя

@app.route("/mailing", methods=['POST', ])
def mass_mailing():
    list_of_emails = list()
    users = User.query.all()
    username_filter = request.args.get('username')
    if username_filter:
        users = User.query.filter(User.username.ilike(f'%{username_filter}%'))
    for user in users:
        list_of_emails.append(user.email)
    email_data = {
            'subject': 'CELERY TEST',
            'body': 'Привет, отправляю тебе это письмо из моего Flask приложения'
    }
    result = send_async_email.delay(list_of_emails, email_data)
    return f"Mailing started, use following ID for tracking: {result.id}"


@app.route("/mailing/<task_id>", methods=['GET', ])
def mailing_result(task_id):
    task = send_async_email.AsyncResult(task_id)
    status_of_task = task.state
    return f"The status of your mailing is: {status_of_task}"


class UserView(MethodView):

    def get(self, user_id):
        user = User.by_id(user_id)
        return jsonify(user.to_dict())

    @validate('json', USER_CREATE)
    def post(self):
        print(request)
        user = User(**request.json)
        user.set_password(request.json['password'])
        user.add()
        return jsonify(user.to_dict())


class AdView(MethodView):

    def get(self, ad_id):
        ad = Ad.by_id(ad_id)
        return jsonify(ad.to_dict())

    @validate('json', AD_CREATE)
    def post(self):
        ad = Ad(**request.json)
        ad.add()
        return jsonify(ad.to_dict())

    def delete(self, ad_id):
        ad = Ad.by_id(ad_id)
        ad.delete()
        return jsonify({'message': f'Ad was deleted'})


app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('users_get'))
app.add_url_rule('/users', view_func=UserView.as_view('users_create'))

app.add_url_rule('/ads', view_func=AdView.as_view('ads_create'))
app.add_url_rule('/ads/<int:ad_id>', view_func=AdView.as_view('get_ad'))
app.add_url_rule('/ads/<int:ad_id>', view_func=AdView.as_view('ads_delete'))
