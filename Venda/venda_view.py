from fastapi import APIRouter
from typing import List
from Venda.venda_controller import VendaController
from Venda.venda_model import Venda
from connector.database import db

venda_controller = VendaController(db)

router = APIRouter()

@router.get("/vendas", response_model=List[Venda])
def listar_vendas():
    return venda_controller.get_all()

