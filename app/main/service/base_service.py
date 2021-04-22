import datetime
import uuid

class BaseService:
    _datetime = datetime
    _uuid = uuid

    def __init__(self):
        pass

    def response_json(self, status, msg, code=200, aditional_param = None):
        if aditional_param and type(aditional_param) != dict:
            raise TypeError('`aditional_param` must be a dict')

        response_object = {
            'status': status,
            'msg': msg,
        }

        if aditional_param is not None:
            for key, single_param in aditional_param.items():
                response_object[key] = single_param

        return response_object, code
