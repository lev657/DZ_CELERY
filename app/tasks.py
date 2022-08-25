from flask_mail import Message
from app import app, mail
from app import celery

'''Команда для запуска: celery -A app.tasks.celery  worker --loglevel=INFO'''


@celery.task(name='tasks.send_async_email')
def send_async_email(emails, email_data):
    for address in emails:
        email = list()
        email.append(address)
        msg = Message(email_data['subject'],
                      sender=app.config['MAIL_DEFAULT_SENDER'],
                      recipients=email)
        msg.body = email_data['body']
        with app.app_context():
            mail.send(msg)
