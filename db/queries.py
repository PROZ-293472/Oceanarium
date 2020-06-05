class Queries:
    query_login_page = "SELECT id_stanowisko FROM Pracownicy WHERE id_pracownika = :id AND haslo = :password"

