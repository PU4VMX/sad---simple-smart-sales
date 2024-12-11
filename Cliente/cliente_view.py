from typing import List
from fastapi import APIRouter

from Cliente.cliente_controller import ClienteController
from Cliente.cliente_model import Cliente
from connector.database import db


cliente_controller = ClienteController(db)

# Criar o roteador FastAPI
router = APIRouter()

@router.get("/clientes", response_model=List[Cliente])
def listar_produtos():
    return cliente_controller.get_all()


#clientes com mais compras
@router.get("/clientes/mais-compras", response_model=List[Cliente])
def listar_clientes_mais_compras():
    return cliente_controller.mais_compraram()