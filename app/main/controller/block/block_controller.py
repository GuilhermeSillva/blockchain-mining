from app.main.service.block.block_service import BlockService
from app.main.util.dto.block_dto import BlockDto
from app.main.controller.base_controller import BaseController


api = BlockDto.api
_block = BlockDto.block

@api.route('/register')
class CreateBlock(BaseController._resource, BaseController):
    @api.response(201, 'Block criado com sucesso')
    @api.doc('create a new block')
    @api.expect(_block, validate=True)
    def post(self):
        block_service = BlockService()
        data = self._req.json
        return block_service.create_new_block(data)