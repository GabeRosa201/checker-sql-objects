import time
from checker.database import Database
from infra.connection import Connection

if __name__ == '__main__':
    print('A verrudara dos arquivos irá começar em breve')

    time.sleep(3)

    # Operação

    # Informar a base modelo
    base_modelo = Database()


    base_a_ser_comparada = Database()

    conn = Connection()
    
    # Se conecta na base de dados
    conn.connect_database(
        base_modelo.get_connection_string_sql()
    )

    # Obtem os dados de todos as procedures

    # Obtem as procedures desta bases

    # Obtem as views dessa base

    # Obtem as tabelas dessa base

    # Obtem as procedures dessa base

    

    print('Obrigado por utilizar nosso sistema!')