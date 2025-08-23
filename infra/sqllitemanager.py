import sqlite3
import os

class SQLiteManager:
    """
    Uma classe para gerenciar a conexão e as operações com um banco de dados SQLite,
    selecionando o arquivo do banco de dados com base no ambiente (desenvolvimento/produção).
    """
    def __init__(self):
        """
        Inicializa o gerenciador, definindo o nome do arquivo do banco de dados
        com base na variável de ambiente 'APP_ENV'.
        """
        # Verifica a variável de ambiente 'APP_ENV'
        env = os.getenv('APP_ENV', 'desenvolvimento') # Padrão é 'desenvolvimento'

        if env == 'producao':
            self.db_file = 'producao.db'
            print("Conectando ao banco de dados de PRODUÇÃO.")
        else:
            self.db_file = 'desenvolvimento.db'
            print("Conectando ao banco de dados de DESENVOLVIMENTO.")
        
        self.connection = None
        self.cursor = None

    def connect(self):
        """
        Estabelece a conexão com o banco de dados e cria o cursor.
        O arquivo do banco será criado se não existir.
        """
        try:
            self.connection = sqlite3.connect(self.db_file)
            # Isso permite acessar os resultados por nome de coluna, como um dicionário
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
            # print(f"Conexão com '{self.db_file}' bem-sucedida!")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados SQLite: {e}")
            raise

    def disconnect(self):
        """
        Fecha a conexão com o banco de dados, se estiver aberta.
        """
        if self.connection:
            self.connection.close()
            # print(f"Conexão com '{self.db_file}' fechada.")

    def execute_query(self, query, params=None):
        """
        Executa uma consulta que modifica o banco de dados (INSERT, UPDATE, DELETE).

        Args:
            query (str): A string da consulta SQL.
            params (tuple, optional): Os parâmetros para a consulta para evitar SQL Injection.

        Returns:
            int: O ID da última linha inserida.
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            self.connection.rollback()
            raise

    def fetch_all(self, query, params=None):
        """
        Executa uma consulta SELECT e retorna todas as linhas como uma lista de dicionários.

        Args:
            query (str): A string da consulta SQL.
            params (tuple, optional): Os parâmetros para a consulta.

        Returns:
            list: Uma lista de linhas, onde cada linha é um objeto semelhante a um dicionário.
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            # A conversão para dict é útil para serialização (ex: API JSON)
            return [dict(row) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Erro ao buscar dados: {e}")
            raise

    def fetch_one(self, query, params=None):
        """
        Executa uma consulta SELECT e retorna a primeira linha como um dicionário.

        Args:
            query (str): A string da consulta SQL.
            params (tuple, optional): Os parâmetros para a consulta.

        Returns:
            dict: Um objeto semelhante a um dicionário para a primeira linha, ou None se não houver resultados.
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except sqlite3.Error as e:
            print(f"Erro ao buscar dado: {e}")
            raise

    def __enter__(self):
        """
        Permite o uso da classe com a instrução 'with', abrindo a conexão.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Garante que a conexão seja fechada ao sair do bloco 'with'.
        """
        self.disconnect()