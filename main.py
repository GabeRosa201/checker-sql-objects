import time
from infra.connection import Connection

if __name__ == '__main__':
    print('A verrudara dos arquivos irá começar em breve')

    time.sleep(3)

    # Operação

    # Informar a base modelo
    base_modelo = {
        'nome': '',
        'server': '',
        'user': '',
        'secret': '',
        'is_windows_auth': False
    }

    base_a_ser_comparada = {
        'nome': '',
        'server': '',
        'user': '',
        'secret': '',
        'is_windows_auth': False
    }

    conn = Connection()
    conn.connect_database(
        base_modelo['nome'],
        base_modelo['server'],
        '',
        '',
        base_modelo['is_windows_auth']
    )

    print('Obrigado por utilizar nosso sistema!')