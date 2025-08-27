from src.checker.database import Database

class TestDatabase():
    def test_database_get_connection_string_is_ok(self):
        database = Database(
            'database-test',
            'server-test',
            'user-test',
            'pwd-test'
        )
        conn_string_test = database.get_connection_string_sql()
        conn_string_expected = 'DRIVER={ODBC Driver 18 for SQL Server};\
SERVER=server-test;\
DATABASE=database-test;\
UID=user-test;\
PWD=pwd-test'
        assert conn_string_test == conn_string_expected

    def test_database_get_connection_string_is_empty(self):
        database = Database(
            'database-test',
            'server-test',
            'user=test',
            'pwd-test'
        )
        conn_string_test = database.get_connection_string_sql()
        conn_string_expected = ''
        assert conn_string_test != conn_string_expected
