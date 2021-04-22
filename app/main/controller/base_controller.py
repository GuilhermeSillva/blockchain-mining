from flask_restplus import Resource
from flask import request

class BaseController:
    _resource = Resource
    _req = request

    def __init__(self):
        pass
