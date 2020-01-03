# 创建多个表并包含Fk、M2M关系
import json
import datetime
from sqlalchemy import create_engine,Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index,Numeric,PrimaryKeyConstraint,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker,scoped_session
from sqlalchemy.types import TypeDecorator, VARCHAR
import os
from config import config


Base = declarative_base()
configDto,err=config.Config().read(env=os.getenv("FLASK_ENV"))
conn ="mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8"% (configDto.mysql.user,
configDto.mysql.passwd,configDto.mysql.host,configDto.mysql.port,configDto.mysql.dbName)
engine = create_engine(conn) 
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class JSONEncodedDict(TypeDecorator):
    "Represents an immutable structure as a json-encoded string."

    impl = VARCHAR(1000)

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value

# ##################### 单表示例 #########################
class Fruit(Base):
    __tablename__ = 'fruit'

    id=Column("id",Integer)
    code=Column(String(255))
    name = Column(String(255))
    color = Column(String(255))
    price = Column(Integer) #Numeric(precision=18, scale=2)

    storeCode = Column("store_code",String(255))
    createdAt = Column("created_at",DateTime, default=func.now())
    updatedAt = Column("updated_at",DateTime, onupdate=func.now())

    __table_args__ = (
        PrimaryKeyConstraint('id'),
        {},
    )

    def __init__(self,code="",name="",color="",price="",storeCode=""):
        self.code = code
        self.name =name
        self.color =color
        self.price =price
        self.storeCode =storeCode


    def __eq__(self,other):
        return self.code == other.code \
        and self.name == other.name \
        and self.color == other.color \
        and self.price == other.price \
        and self.storeCode == other.storeCode


    @classmethod
    def toDict(self,obj):
        if hasattr(obj, '__dict__'):
            dict = obj.__dict__
        return dict
    
    @classmethod
    def fromDict(self,dict):
        obj = Fruit()
        obj.__dict__.update(dict)
        return obj

def init():
    try:
        Base.metadata.create_all(engine)
        return None
    except Exception as inst:
        return str(inst)



