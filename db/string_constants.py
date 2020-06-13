class ColumnNames():
    def __init__(self):
        self.pracownicy_db = list(['id_pracownika', 'imie', 'nazwisko', 'pesel', 'data_urodzenia', 'nr_licencji',
                                   'id_oceanarium', 'id_adresu', 'id_stanowisko'])
        self.pracownicy_display = list(['ID', 'Imię', 'Nazwisko', 'PESEL', 'Data urodzenia', 'Nr licencji',
                                        'ID oceanarium', 'ID adresu', 'ID stanowiska'])
        self.pracownicy_password = 'haslo'

        self.akwaria_db = list(['id_akwarium', 'nazwa_akwarium', 'objectosc', 'temperatura_wody',
                                'id_oceanarium', 'nazwa_sekcji'])
        self.akwaria_display = list(['ID', 'Nazwa akwarium', 'Objętość', 'Temperatura wody',
                                     'ID oceanarium', 'Nazwa sekcji'])
        self.zwierzeta_db = list(['id_zwierzecia', 'nazwa_zwierzecia', 'data_urodzenia',
                                       'plec', 'dlugosc', 'waga', 'id_akwarium', 'id_gatunku'])
        self.zwierzeta_display = list(['ID', 'Nazwa', 'Data urodzenia', 'Płeć', 'Długość (m)','Waga (kg)',
                                       'ID akwarium', 'ID gatunku'])

        self.db_strings = list([self.pracownicy_db,self.akwaria_db,self.zwierzeta_db])
        self.display_strings = list([self.pracownicy_display, self.akwaria_display, self.zwierzeta_display])
        self.tables = ['Pracownicy','Akwaria','Zwierzeta']

    def get_column_headers(self, table, columns):
        table_index = self.tables.index(table)
        all_names_db = self.db_strings[table_index]
        all_names_display = self.display_strings[table_index]
        headers = list()
        if columns == ['*']:
            headers = all_names_display
            return headers
        col_names = columns[0].split(',')
        for header in col_names:
            index = all_names_db.index(header)
            headers.append(all_names_display[index])
        return headers

    def get_db_column_name(self,table,column_name):
        table_index = self.tables.index(table)
        col_index = self.display_strings[table_index].index(column_name)
        return self.db_strings[table_index][col_index]


    def get_id_name(self,table):
        table_index = self.tables.index(table)
        return self.db_strings[table_index][0]
