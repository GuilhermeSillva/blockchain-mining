from flask_restplus import Api
from flask import Blueprint

#controllers
from .main.controller.block.block_controller import api as block_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
    title='Blockchaing and mining',
    version='1.0'
)

api.add_namespace(block_ns, path='/block')
