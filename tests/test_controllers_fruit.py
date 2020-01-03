import unittest
from flask import Flask,Blueprint
from flask_restful import reqparse, abort, Api, Resource
import json
from controllers import fruit


"""
py.test.exe .\test_proxy_manage.py -s
"""

class TestControllerIpPort(unittest.TestCase):

    """{'success': True, 'error': {'code': None, 'message': None, 'detail': None}, 'result': [{'code': 'bb', 'name': 'bear', 'color': None, 'price': 1, 'storeCode': None, 'createdAt': 'Fri, 03 Jan 2020 10:05:57 -0000', 'updatedAt': 'Fri, 03 Jan 2020 10:05:59 -0000'}, {'code': 'aa', 'name': 'apple', 'color': None, 'price': 1, 'storeCode': None, 'createdAt': 'Fri, 03 Jan 2020 10:05:55 -0000', 'updatedAt': 'Fri, 03 Jan 2020 10:05:56 -0000'}]}"""
    def testGet(self):

        app = Flask(__name__)
        api = Api(app)
        with app.test_request_context("/?maxResultCount=2"):

            wrapper = api.output(fruit.FruitApi().get)
            resp = wrapper()
            self.assertEqual(resp.status_code, 200)
            d =resp.data.decode()
            j = json.loads(d)
            self.assertEqual(j.get("success"),True)
            self.assertEqual(len(j.get("result")),2)
            