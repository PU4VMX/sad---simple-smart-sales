
from datetime import datetime
from utils.basemodel import BaseSchema


class Venda(BaseSchema):
    id: int
    id_produto: int = None
    id_cliente: int = None
    nome_cliente: str = None
    nome_produto: str = None
    quantidade: int
    data_venda: datetime