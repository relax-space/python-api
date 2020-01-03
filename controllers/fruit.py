from flask_restful import reqparse,  Resource,fields, marshal_with
import json
import logging
from models import model,fruit
from controllers import utils,api_error


parser = reqparse.RequestParser()
parser.add_argument('skipCount')
parser.add_argument('maxResultCount')

ipPortFields ={
    "code":fields.String,
    "name":fields.String,
    "color":fields.String,
    "price":fields.Integer,
    "storeCode":fields.String,
    "createdAt":fields.DateTime,
    "updatedAt":fields.DateTime,
}
errFields ={
        'code': fields.String,
        'message': fields.String,
        'detail': fields.String,
    }
respFields = {
    'success': fields.Boolean,
    'error': fields.Nested(errFields),
    'result': fields.List(fields.Nested(ipPortFields)),
}


class FruitApi(Resource):
    @marshal_with(respFields)
    def get(self):
        
        args = parser.parse_args()
        offset,err = utils.getIntNone(args.get("skipCount"))
        if err != None:
            return utils.returnFail(400,api_error.invalidParamError("skipCount",args.get("skipCount"),err))
        limit,err = utils.getIntNone(args.get("maxResultCount"))
        if err != None:
            return utils.returnFail(400,api_error.invalidParamError("maxResultCount",args.get("maxResultCount"),err))
        if limit ==0:
            limit=100
        session = model.Session()
        list,err=fruit.FruitOp().getAll(session,offset,limit)
        if err != None:
            return utils.returnFail(500,api_error.unknownError(err))
        return utils.returnSucc(200,list)

    
    

