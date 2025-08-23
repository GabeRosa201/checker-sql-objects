
class Comparator():

    def __init__(self):
        pass

    def _compare_missing_values(self,
                                lista_to_compare:list[str],
                                lista_to_check:list[str]) -> list[str]:
        """
        Método que compara quais os valores que estão faltando dentro de uma lista
        """
        pass

    def compare_tables(self, 
                       tables_original:list[str],
                       tables_missing:list[str]) -> list[str]:
        
        if len(tables_original) > 0:

            tables_missing = self._compare_missing_values(tables_original, tables_missing)

            return tables_missing
        
        return []
        
