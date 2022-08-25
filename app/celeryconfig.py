from kombu import Queue, Exchange

task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
)

result_backend = 'redis://localhost:6379/0'
broker_url = 'redis://localhost:6379/1'
