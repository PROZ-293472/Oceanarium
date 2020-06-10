class ColumnNames():
    def __init__(self):
        self.pracownicy_db = list(['id_pracownika', 'imie', 'nazwisko', 'pesel', 'data_urodzenia', 'nr_licencji',
                                   'id_oceanarium','id_adresu', 'id_stanowisko'])
        self.pracownicy_display = list(['ID', 'Imię', 'Nazwisko', 'PESEL', 'Data urodzenia', 'Nr licencji',
                                     'ID oceanarium', 'ID adresu', 'ID stanowiska'])

    def get_column_headers(self,table,columns) :
        headers = list()
        col_names = columns[0].split(',')
        for header in col_names:
            index = self.pracownicy_db.index(header)
            headers.append(self.pracownicy_display[index])
        return headers

