from threading import Thread
from flask import Flask, jsonify, request
from flask_cors import CORS
import logging, json
from pprint import pformat
from app.config import Config
# import pika

cors=CORS()
def create_app():
    app = Flask(__name__)
    
    # set logger
    logger = logging.getLogger('gunicorn.error')
    logger.setLevel(logging.INFO)
    # loggingStreamHandler = logging.StreamHandler()
    # to save to file
    # loggingStreamHandler = logging.FileHandler("test.json",mode='a')
    # class JSONFormatter(logging.Formatter):
    #     def __init__(self):
    #         super().__init__()
    #     def format(self, record):
    #         # record.msg = json.dumps(record.msg)
    #         # return super().format(record)
    #         return pformat(record.msg)
    # loggingStreamHandler.setFormatter(JSONFormatter())
    # logger.addHandler(loggingStreamHandler)
    # app.logger = logger

    # Loading environment vars
    app.config.from_object(Config)

    # init cors
    cors.init_app(app)
    
    with app.app_context():
        from app.routes import app_routes
        return app

app = create_app()
