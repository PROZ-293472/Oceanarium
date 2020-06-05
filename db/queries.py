class Queries:
    query_login_page = "SELECT id_stanowisko FROM Pracownicy WHERE id_pracownika = :id AND haslo = :password"
    query_get_tables = "SELECT table_name FROM user_tables ORDER BY table_name"
    query_get_list = "SELECT {cols} FROM {table} ORDER BY {param}"

