from flask_restplus import Api
from flask import Blueprint

#controllers


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
    title='Blockchaing and mining',
    version='1.0'
)
