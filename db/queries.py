class Queries:
    query_login_page = "SELECT id_stanowisko FROM Pracownicy WHERE id_pracownika = :id AND haslo = :password"
    query_get_tables = "SELECT table_name FROM user_tables ORDER BY table_name"
    query_get_list = "SELECT {cols} FROM {table} ORDER BY {param}"
    query_delete_row = "DELETE FROM {table} WHERE {id_name} = {id}"
    query_edit_value = "UPDATE {table} SET {column_name} = '{new_value}' WHERE {id_name} = {id}"
    query_add_row = "INSERT INTO {table} VALUES ({values})"

    query_trainer_personal = "SELECT imie,nazwisko, PESEL, data_urodzenia, nr_licencji FROM Pracownicy " \
                             "WHERE id_pracownika = :id"
    query_trainer_animals = "SELECT nazwa_zwierzecia, plec, id_akwarium, nazwa_gatunku FROM Opieka o " \
                            "INNER JOIN Zwierzeta z ON o.id_zwierzecia = z.id_zwierzecia " \
                            "INNER JOIN Gatunki g ON z.id_gatunku = g.id_gatunku " \
                            "WHERE o.id_pracownika = :id"

