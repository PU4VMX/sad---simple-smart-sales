


from utils.basemodel import BaseSchema


class Produto(BaseSchema):
    id: int
    nome: str
    preco: float
    quantidade_em_estoque: int