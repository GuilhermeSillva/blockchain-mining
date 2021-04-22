from app.main.config import env
import datetime
import uuid

class BaseService:
    _datetime = datetime
    _uuid = uuid
    __env = env

    def __init__(self):
        pass

    def response_json(self, status, msg=None, code=200, aditional_param = None, error=None):
        if aditional_param and type(aditional_param) != dict:
            raise TypeError('`aditional_param` must be a dict')

        response_object = {'status': status}

        if msg is not None:
            response_object['msg'] = msg

        if aditional_param is not None:
            response_object['data'] = {}
            for key, single_param in aditional_param.items():
                response_object['data'][key] = single_param

        if error is not None and self.__env == 'dev':
           response_object['error'] = str(error)

        return response_object, code

