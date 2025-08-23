class SqlliteManager():

    def __init__(self):
        pass

    def config_database(self):
        """
        Cria todas as tabelas do banco de dados, caso no ambiente não houver
        """

        self.create_table_databases(self)

        pass

    def create_table_databases(self):
        query_create_table = """
            CREATE TABLE IF NOT EXISTS databases 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                server TEXT NOT NULL,
                database_name TEXT NOT NULL
            )
        """
        pass

