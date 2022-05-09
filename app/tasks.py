from app.celery_app import celery
import time
from app.config import Config
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

@celery.task()
def add(x, y):
    res = { "data": x + y }
    logger.info(f"Celery task ADD:{res}")
    # time.sleep(100000000)
    return res

@celery.task()
def mul(x, y):
    return x * y

