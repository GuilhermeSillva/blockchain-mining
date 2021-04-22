from flask_restplus import Namespace, fields

class BlockDto:
    api = Namespace('block', description='block related operations')
    block = api.model('block', {
        # 'index': fields.String(description='index block'),
        # 'public_id': fields.String(description='block identifier'),
        # 'previous_hash': fields.String(description='previous hash block'),
        'data': fields.String(required=True, description='dado que sera salvo.'),
        # 'created_at': fields.String(description='block creation date'),
        # 'hash': fields.String(description='current block hash')
    })