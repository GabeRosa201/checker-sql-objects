import pyodbc

class Connection():

    def __init__(self):
        self._connection = None
        self._driver = 'ODBC Driver 17 for SQL Server'
        pass

    def connect_database(self, 
                         database:str, 
                         server:str, 
                         user: str,
                         pwd: str,
                         is_windows_auth: str):
        
        """
        Estabelece a conexão com o SQL Server.
        """
        try:
            if user and pwd:
                self._connection = pyodbc.connect(
                    f"DRIVER={{{self._driver}}};"
                    f"SERVER={server};"
                    f"DATABASE={database};"
                    f"UID={user};"
                    f"PWD={is_windows_auth};"
                )
            else:
                # Autenticação integrada do Windows
                self._connection = pyodbc.connect(
                    f"DRIVER={{{self._driver}}};"
                    f"SERVER={server};"
                    f"DATABASE={database};"
                    f"Trusted_Connection=yes;"
                )

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