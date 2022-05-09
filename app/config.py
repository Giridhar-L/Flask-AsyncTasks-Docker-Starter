import os, urllib.parse
class Config(object):
    CELERY_BROKER_URL: str = os.environ.get('CELERY_BROKER_URL')
    CELERY_BACKEND_URL: str = os.environ.get('CELERY_BACKEND_URL')





