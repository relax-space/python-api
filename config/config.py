
import yaml,os

class DbDto:
    def __init__(self,host=None,port=None,
    user=None,passwd=None,dbName=None):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.dbName=dbName
class ConfigDto:
    def __init__(self,mysql=None,serviceName=None,httpport=None):
        self.mysql =mysql
        self.serviceName=serviceName
        self.httpport=httpport


class Config:
    def __init__(self):
        pass
        
    def read(self,env=None):
        path ="config.yml"
        if env !=None and env != "":
            path = "config.%s.yml" % (env)
        cfg = None
        cfgDto=None
        try:
            path = os.getcwd()+"/"+path
            with open(path,"r") as ymlfile:
                cfg =yaml.safe_load(ymlfile)
            mysqlDto = cfg.get("mysql")
            if mysqlDto ==None:
                return None,error.miss("mysql section")
            cfgDto =ConfigDto(
                mysql=DbDto(
                    host=mysqlDto.get("host"),
                    port=mysqlDto.get("port"),
                    user=mysqlDto.get("user"),
                    passwd=mysqlDto.get("passwd"),
                    dbName=mysqlDto.get("dbName"),
                ),
                serviceName=cfg.get("serviceName"),
                httpport=cfg.get("httpport"),
            )
        except Exception as inst:
            return None,str(inst)
        return cfgDto,None
