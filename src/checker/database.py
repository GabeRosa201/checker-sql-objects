
class Database():

    def __init__(self, database:str, server:str, user:str, pwd:str, auth_windows:bool=False):
        self._database = database
        self._server = server
        self._user = user
        self._pwd = pwd
        self._is_auth_windows = auth_windows

    def get_connection_string_sql(self):
        if not self._is_auth_windows:
            return f'DRIVER={{ODBC Driver 18 for SQL Server}};\
SERVER={self._server};\
DATABASE={self._database};\
UID={self._user};\
PWD={self._pwd}'
        else:
            # Autenticação integrada do Windows
            return f'DRIVER={{ODBC Driver 18 for SQL Server}};\
                SERVER={self._server};\
                DATABASE={self._database};\
                Trusted_Connection=yes;'

    def get_procedures_from_base(self):

        query_via_proc = """
            EXEC sp_stored_procedures
        """

        query_via_select = """
            SELECT name FROM sys.procedures
        """
        pass

    def get_procedure_content(self, procedure_name):
        """
        A execução da procedure devolve uma coluna chamada text
        onde cada linha corresponde a uma linha mapeada na procedure
        """

        query = """
            EXEC sp_helptext 
        """
        pass

    def get_tables_from_base(self):
        """
        Metodo que obtem uma lista de tabelas que foram criadas em determinada base
        """

        query = """

        """
        pass

