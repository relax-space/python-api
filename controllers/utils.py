from flask import Response
import json
from controllers.type_result import Error,Result

def returnFail(status,err):
    return Result(success=False, error=err,result=None),status

def returnSucc(status,result):
    return Result(success=True,error=None, result=result),status

def containStr(list,str):
    for s in list:
        if s == str:
            return True
    return False

def getInt(s):
    try:
        v = int(s)
        return v,None
    except Exception as inst:
        return None,str(inst)

def getIntNone(s):
    try:
        if s ==None:
            return 0,None
        v = int(s)
        return v,None
    except Exception as inst:
        return None,str(inst)