from typing import List

from Produto.produto_model import Produto


class ProdutoController:
    def __init__(self, database):
        self.database = database

    def get_all(self) -> List[Produto]:
        query = "SELECT * FROM produtos"
        produtos = self.database.fetchall(query)
        return [
            Produto(
                **dict(zip(["id", "nome", "preco", "quantidade_em_estoque"], produto))
            )
            for produto in produtos
        ]

    # 10 produtos mais vendidos
    def mais_vendidos(self) -> List[Produto]:
        query = """
        SELECT p.id, p.nome, p.preco, p.quantidade_em_estoque, COUNT(v.id_produto) AS vendas, SUM(v.quantidade) AS quantidade_vendida
        FROM produtos p LEFT JOIN vendas v ON p.id = v.id_produto
        GROUP BY p.id
        ORDER BY quantidade_vendida DESC
        LIMIT 10;
        """
        produtos = self.database.fetchall(query)
        return [
            Produto(
                **dict(zip(["id", "nome", "preco", "quantidade_em_estoque"], produto))
            )
            for produto in produtos
         ]
    

    # top 10 produtos com baixo estoque
    def baixo_estoque(self) -> List[Produto]:
        query = """
        SELECT * FROM produtos ORDER BY quantidade_em_estoque ASC LIMIT 10;
        """
        produtos = self.database.fetchall(query)
        return [
            Produto(
                **dict(zip(["id", "nome", "preco", "quantidade_em_estoque"], produto))
            )
            for produto in produtos
        ]

    
