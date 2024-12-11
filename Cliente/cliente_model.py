from utils.basemodel import BaseSchema

class Cliente(BaseSchema):
    id: int
    nome: str
    email: str
    quantidade_comprada: int = None