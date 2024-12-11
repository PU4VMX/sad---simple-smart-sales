import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self, host, database, user, password):
        """Inicializa a classe com os parâmetros de conexão ao banco de dados"""
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self):
        """Estabelece a conexão com o banco de dados"""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            print("Conexão com o banco de dados estabelecida com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
    
    def close(self):
        """Fecha a conexão com o banco de dados"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexão com o banco de dados fechada.")

    def execute_query(self, query, params=None):
        """
        Executa uma consulta SQL com parâmetros para evitar SQL Injection.
        :param query: A query SQL a ser executada.
        :param params: Os parâmetros a serem passados para a query (se necessário).
        :return: O resultado da execução da consulta (se houver).
        """
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print("Consulta executada com sucesso!")
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")
            self.connection.rollback()

    def fetchall(self, query, params=None):
        """
        Executa uma consulta SELECT e retorna todos os resultados.
        :param query: A consulta SQL a ser executada.
        :param params: Os parâmetros para a consulta (se necessário).
        :return: Lista com os resultados da consulta.
        """
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")
            return None

    def fetchone(self, query, params=None):
        """
        Executa uma consulta SELECT e retorna o primeiro resultado.
        :param query: A consulta SQL a ser executada.
        :param params: Os parâmetros para a consulta (se necessário).
        :return: O primeiro resultado da consulta.
        """
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar dado: {e}")
            return None

    def insert_data(self, table, data):
        """
        Insere dados de forma segura na tabela.
        :param table: O nome da tabela onde os dados serão inseridos.
        :param data: Um dicionário contendo os dados a serem inseridos (nome_coluna: valor).
        """
        columns = data.keys()
        values = [data[column] for column in columns]
        
        # Usando sql.SQL para evitar SQL Injection
        insert_query = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({placeholders})").format(
            table=sql.Identifier(table),
            fields=sql.SQL(', ').join(map(sql.Identifier, columns)),
            placeholders=sql.SQL(', ').join(sql.Placeholder() for _ in columns)
        )
        
        self.execute_query(insert_query, values)


# Exemplo de uso
db = Database(host="localhost", database="sistema_vendas", user="postgres", password="postgres")
db.connect()

