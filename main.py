from flask import Flask,Blueprint
from flask_restful import reqparse, abort, Api, Resource
import logging
from controllers import fruit,ping
from models import model


app = Flask(__name__)
apiBp = Blueprint('api', __name__)
api = Api(apiBp)

def init():
    api.add_resource(fruit.FruitApi, '/')
    api.add_resource(ping.PingApi, '/ping')

def start():
    try:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        logging.info("web api start...")
        err=model.init()
        if err != None:
            logging.error(err)
            return
        init()
        app.register_blueprint(apiBp)
        app.run(host="0.0.0.0",port=8080)
    except Exception as inst:
        raise inst

if __name__ == "__main__":
    start()
    
