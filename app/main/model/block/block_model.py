from app.main.model.base_model import BaseModel
from app.main.util.crypt.crypt_helper import CryptHelper
from app.main import data_base

class BlockModel(data_base.Model, BaseModel):
    __tablename__ = 'block'

    id = data_base.Column(data_base.Integer, primary_key=True, autoincrement=True)
    index =  data_base.Column(data_base.Integer, unique=True, index=True)
    public_id = data_base.Column(data_base.String(255), unique=True, index=True)
    previous_hash = data_base.Column(data_base.String(255), unique=True, index=True)
    data = data_base.Column(data_base.String(255))
    created_at = data_base.Column(data_base.DateTime, nullable=False)
    hash = data_base.Column(data_base.String(255), unique=True, index=True)

    def get_previous_block_info(self):
        return super().select().query(BlockModel.previous_hash, BlockModel.index).order_by(BlockModel.id.desc()).limit(1).scalar()
