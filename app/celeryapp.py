from celery import Celery


celery = Celery(
        'celery_app',
        backend='redis://localhost:6379/0',
        broker='redis://localhost:6379/1',
    )
