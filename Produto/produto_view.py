# app/views.py
from fastapi import APIRouter
from typing import List
from Produto.produto_controller import ProdutoController
from Produto.produto_model import Produto
from connector.database import db


produto_controller = ProdutoController(db)

# Criar o roteador FastAPI
router = APIRouter()

@router.get("/produtos", response_model=List[Produto])
def listar_produtos():
    return produto_controller.get_all()


# 10 produtos mais vendidos
@router.get("/produtos/mais-vendidos", response_model=List[Produto])
def listar_produtos_mais_vendidos():
    return produto_controller.mais_vendidos()

# top 10 produtos com baixo estoque
@router.get("/produtos/baixo-estoque", response_model=List[Produto])
def listar_produtos_baixo_estoque():
    return produto_controller.baixo_estoque()