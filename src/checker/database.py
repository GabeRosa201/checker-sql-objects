
class Database():

    def __init__(self):
        pass

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

