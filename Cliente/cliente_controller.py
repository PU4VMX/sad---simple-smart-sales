from typing import List

from Cliente.cliente_model import Cliente

class ClienteController:
    def __init__(self, database):
        self.database = database

    
    def get_all(self) -> List[Cliente]:
        query = "SELECT * FROM clientes"
        clientes = self.database.fetchall(query)
        return [
            Cliente(
                **dict(zip(["id", "nome", "email"], cliente))
            )
            for cliente in clientes
        ]
    

    #clientes que mais compraram
    def mais_compraram(self) -> List[Cliente]:
        query = """
        SELECT c.id, c.nome, c.email, COUNT(v.id_cliente) AS compras, SUM(v.quantidade) AS quantidade_comprada
        FROM clientes c LEFT JOIN vendas v ON c.id = v.id_cliente
        GROUP BY c.id
        ORDER BY quantidade_comprada DESC
        LIMIT 10;
        """
        clientes = self.database.fetchall(query)
        return [
            Cliente(
                **dict(zip(["id", "nome", "email", "quantidade_comprada"], cliente))
            )
            for cliente in clientes
        ]
    

