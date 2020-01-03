import unittest
import json
from models import model,fruit

"""
py.test.exe .\test_models_fruit.py -s
"""


class TestFruit(unittest.TestCase):
    def testGetAll(self):
        session = model.Session()
        fruitList,err=fruit.FruitOp().getAll(session,0,2)
        self.assertIsNone(err)
        self.assertEqual(len(fruitList),2)
        print("===>getall",fruitList)
    
