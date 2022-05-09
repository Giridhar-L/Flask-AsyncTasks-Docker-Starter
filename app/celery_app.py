from celery import Celery
from app.config import Config
import os,ssl

# cert_path = os.path.join(os.path.dirname(__file__), './db/tmpmongocert.txt')
# amqpURL = 'amqp://myuser:mypassword@host.docker.internal:5672/'
# mongoUrl= "mongodb://root:rootpassword@host.docker.internal:27017/"

backendUrl = Config.CELERY_BROKER_URL
brokerUrl = Config.CELERY_BACKEND_URL

class CeleryConfig:
    imports = ('app.tasks')
    result_expires = 0
    accept_content = ['json', 'msgpack', 'yaml']
    task_serializer = 'json'
    result_serializer = 'json'
    timezone = 'Asia/Kolkata'
    enable_utc = True
    # !!Important for backend
    task_track_started = True

    result_backend = backendUrl
    mongodb_backend_settings = {
        "database": "celery_task_db",
        "taskmeta_collection": "task_metadata",
        # "options" : {
        #     "tls": True, 
        #     "tlsCAFile": cert_path
        # }
    }
    broker_url = brokerUrl
    # broker_use_ssl = {
    #     'cert_reqs': ssl.CERT_REQUIRED,
    #     'certfile': cert_path
    # }

celery = Celery("celery_app")
celery.config_from_object(CeleryConfig)
