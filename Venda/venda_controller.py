from typing import List
from Venda.venda_model import Venda


class VendaController:
    def __init__(self, database):
        self.database = database


    def get_all(self) -> List[Venda]:
        query = """
        SELECT vendas.id, clientes.nome AS nome_cliente, produtos.nome AS nome_produto, vendas.quantidade, vendas.data_venda, vendas.id_cliente, vendas.id_produto
        FROM vendas
        JOIN clientes ON vendas.id_cliente = clientes.id
        JOIN produtos ON vendas.id_produto = produtos.id
        """
        vendas = self.database.fetchall(query)
        return [
            Venda(
                **dict(zip(["id", "nome_cliente", "nome_produto", "quantidade", "data_venda", "id_cliente", "id_produto" ], venda))
            )
            for venda in vendas
        ]
        
  
    def vendas_produto(self, id_produto) -> List[Venda]:
        query = f"SELECT * FROM vendas WHERE id_produto = {id_produto}"
        vendas = self.database.fetchall(query)
        return [
            Venda(
                **dict(zip(["id", "id_produto", "quantidade", "data_venda"], venda))
            )
            for venda in vendas
        ]
        

    def vendas_periodo(self, data_inicio, data_fim) -> List[Venda]:
        query = f"SELECT * FROM vendas WHERE data_venda BETWEEN '{data_inicio}' AND '{data_fim}'"
        vendas = self.database.fetchall(query)
        return [
            Venda(
                **dict(zip(["id", "id_produto", "quantidade", "data_venda"], venda))
            )
            for venda in vendas
        ]