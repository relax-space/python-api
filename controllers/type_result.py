class Error:
    

    def __init__(self,code = 0,message="",detail = object()):
        self.code = code
        self.message = message
        self.detail = detail

    def __str__(self):
        return self.message

    def __eq__(self,other):
        if other == None:
            if self.code == 0 and self.message == "" and self.detail == {}:
                return True
            else:
                return False
        return self.code == other.code and self.message == other.message and self.detail == other.detail
    @classmethod
    def toDict(self,obj):
        dict = obj.__dict__
        return dict
    
    @classmethod
    def fromDict(self,dict):
        obj = Error()
        obj.__dict__.update(dict)
        return obj


class Result:
    

    def __init__(self,success=False,result=None,error=None):
        self.success = success
        self.result = result
        self.error = error
    @classmethod
    def toDict(self,obj):
        dict = obj.__dict__
        return dict
    
    @classmethod
    def fromDict(self,dict):
        obj = Result()
        obj.__dict__.update(dict)
        return obj
