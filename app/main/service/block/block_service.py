from app.main.model.block.block_model import BlockModel
from app.main.service.base_service import BaseService
from app.main.util.crypt.crypt_helper import CryptHelper

class BlockService(BaseService):
    def __init__(self):
        self.block_model = BlockModel()

    def create_new_block(self, data):
        try:
            previous_block_info = self.get_previous_block_info()
            new_block = BlockModel(
                index = int(previous_block_info.index) + 1,
                public_id = str(self._uuid.uuid4()),
                previous_hash = str(previous_block_info.previous_hash),
                data = str(data['data']),
                created_at = self._datetime.datetime.utcnow(),
                hash = CryptHelper.generate_hash(previous_block_info, data)
            )

            public_id = self.block_model.insert(new_block, True)
            return super().response_json(True, 'bloco criado com sucesso', 201, {'public_id': public_id})

        except Exception as e:
            return super().response_json(False, 'Erro ao criar um novo bloco', 500, error=e)

    def get_previous_block_info(self):
        return self.block_model.get_previous_block_info()

