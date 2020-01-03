from sqlalchemy import create_engine
from models.model import Fruit


class FruitOp:
    def __init__(self):
        pass
    
    def insert(self,session,fruit):
        try:
            session.add(fruit)
        except Exception as inst:
            return str(inst)
        return None
        
    
    def get(self,session,code):
        fruit =None
        try:
            fruit=session.query(Fruit).filter(Fruit.code==code).first()
        except Exception as inst:
            return None,str(inst)
        return fruit,None
        

    def getAll(self,session,offset,limit):
        fList =None
        try:
            fList=session.query(Fruit).order_by(Fruit.updatedAt.desc()).limit(limit).offset(offset).all()
        except Exception as inst:
            return None,str(inst)
        return fList,None


