from flask_restful import reqparse,  Resource,fields, marshal_with
import json
import logging

class PingApi(Resource):
    def get(self):
        return "pong"

    
    

