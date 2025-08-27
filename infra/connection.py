import pyodbc

class Connection():

    def __init__(self):
        self._connection = None
        self._driver = 'ODBC Driver 17 for SQL Server'
        pass

    def connect_database(self, connection_string):
        
        """
        Estabelece a conexão com o SQL Server.
        """
        try:
            self._connection = pyodbc.connect(connection_string)

            print("✅ Conexão estabelecida com sucesso!")
            return self._connection
        
        except Exception as e:
            print(f"❌ Erro ao conectar no SQL Server: {e}")
            return None

    def desconect(self):
        if self._connection:
            self._connection.close()
            print("🔒 Conexão fechada.")

    def execute_query(self, query:str, params:list):
        pass