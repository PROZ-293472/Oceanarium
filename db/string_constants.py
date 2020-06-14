from copy import copy

from sympy import pretty_print
from sympy.abc import m


class ColumnNames():
    def __init__(self, mode='Display'):
        self.mode = mode

        self.pracownicy_db = list(['id_pracownika', 'imie', 'nazwisko', 'pesel', 'data_urodzenia', 'nr_licencji',
                                   'id_oceanarium', 'id_adresu', 'id_stanowisko'])
        self.pracownicy_display = list(['ID', 'Imię', 'Nazwisko', 'PESEL', 'Data urodzenia', 'Nr licencji',
                                        'ID oceanarium', 'ID adresu', 'ID stanowiska'])
        self.pracownicy_password = 'haslo'
        self.pracownicy_data_types = list(['int', 'varchar20', 'varchar30', 'char11', 'date', 'varchar30',
                                           'int', 'int', 'int','char64'])
        self.pracownicy_optional = list([False, False, False, True, True, True, False, False, False])

        self.akwaria_db = list(['id_akwarium', 'nazwa_akwarium', 'objectosc', 'temperatura_wody',
                                'id_oceanarium', 'nazwa_sekcji'])
        self.akwaria_display = list(['ID', 'Nazwa akwarium', f'Objętość (m\N{SUPERSCRIPT THREE})',
                                     f'Temperatura \n wody (\N{DEGREE SIGN}C)',
                                     'ID oceanarium', 'Nazwa sekcji'])
        self.akwaria_data_types = list(['int', 'varchar40', 'float', 'float', 'int', 'varchar20'])
        self.akwaria_optional = list([False, False, False, True, False, False])

        self.zwierzeta_db = list(['id_zwierzecia', 'nazwa_zwierzecia', 'data_urodzenia',
                                  'plec', 'dlugosc', 'waga', 'id_akwarium', 'id_gatunku'])
        self.zwierzeta_display = list(['ID', 'Nazwa', 'Data urodzenia', 'Płeć', 'Długość (m)', 'Waga (kg)',
                                       'ID akwarium', 'ID gatunku'])
        self.zwierzeta_data_types = list(['int', 'varchar20', 'date', 'char1', 'float', 'float', 'int', 'int'])
        self.zwierzeta_optional = list([False, False, True, True, True, True, False, False])

        self.pokazy_db = list(['id_pokazu', 'nazwa_pokazu', 'miejsce', 'id_oceanarium'])
        self.pokazy_display = list(['ID', 'Nazwa', 'Miejsce', 'ID oceanarium'])
        self.pokazy_data_types = list(['int', 'varchar30', 'varchar20', 'int'])
        self.pokazy_optional = list([False, False, False, False])

        self.adresy_db = list(['id_adresu', 'miejscowosc', 'kod_pocztowy', 'ulica', 'nr_budynku', 'nr_lokalu'])
        self.adresy_display = list(['ID adresu', 'Miejscowość', 'Kod_pocztowy', 'Ulica', 'Nr budynku', 'Nr lokalu'])
        self.adresy_data_types = list(['int', 'varchar40', 'char6', 'varchar40', 'varchar4', 'varchar5'])
        self.adresy_optional = list([False, False, False, False, False, True])

        self.gatunki_db = list(['id_gatunku', 'nazwa_gatunku', 'nazwa_lacinska', 'rodzaj', 'opis'])
        self.gatunki_display = list(['ID gatunku', 'Nazwa gatunku', 'Nazwa lacinska', 'Rodzaj', 'Opis'])
        self.gatunki_data_types = list(['int', 'varchar40', 'varchar40', 'varchar30', 'varchar400'])
        self.gatunki_optional = list([False, False, False, False, True])

        self.db_strings = list([self.pracownicy_db, self.akwaria_db, self.zwierzeta_db, self.pokazy_db,
                                self.gatunki_db])
        self.display_strings = list(
            [self.pracownicy_display, self.akwaria_display, self.zwierzeta_display, self.pokazy_display,
             self.gatunki_display])
        self.additional_db_strings = list([self.adresy_db, [], self.gatunki_db])
        self.additional_display_strings = list([self.adresy_display, [], self.gatunki_display])
        self.data_types = [self.pracownicy_data_types, self.akwaria_data_types, self.zwierzeta_data_types,
                           self.pokazy_data_types, self.gatunki_data_types]
        self.additional_data_types = [self.adresy_data_types, [], self.gatunki_data_types]
        self.tables = ['Pracownicy', 'Akwaria', 'Zwierzeta', 'Pokazy', 'Gatunki']
        self.additional_tables = ['Adresy', [], 'Gatunki']
        self.tables_optionals = [self.pracownicy_optional, self.akwaria_optional, self.zwierzeta_optional,
                                 self.pokazy_optional, self.gatunki_optional]
        self.additional_tables_optionals = [self.adresy_optional, [], self.gatunki_optional]
    def get_column_headers(self, table, columns):

        table_index = self.tables.index(table)
        table_names_db = self.db_strings[table_index]
        if self.mode == 'Add' and (table_index == 0 or table_index == 2):
            table_names_display = copy(self.display_strings[table_index])
            additional_table_id_name = self.additional_display_strings[table_index][0]
            table_names_display.remove(additional_table_id_name)
            table_names_display = table_names_display + self.additional_display_strings[table_index]
        else:
            table_names_display = self.display_strings[table_index]
        headers = list()
        if columns == ['*']:
            headers = table_names_display
            return headers
        col_names = columns[0].split(',')
        for header in col_names:
            index = table_names_db.index(header)
            headers.append(table_names_display[index])
        return headers

    def get_db_column_name(self, table, column_name):
        table_index = self.tables.index(table)
        col_index = self.display_strings[table_index].index(column_name)
        return self.db_strings[table_index][col_index]

    def get_id_name(self, table):
        table_index = self.tables.index(table)
        return self.db_strings[table_index][0]

    def additional_table_id_name(self, table_index):
        return self.additional_db_strings[table_index][0]

    def get_data_types(self, table):
        if self.tables.__contains__(table):
            return self.data_types[self.tables.index(table)]
        if self.additional_tables.__contains__(table):
            return self.additional_data_types[self.additional_tables.index(table)]

    def get_optionals(self, table):
        if self.tables.__contains__(table):
            return self.tables_optionals[self.tables.index(table)]
        if self.additional_tables.__contains__(table):
            return self.additional_tables_optionals[self.additional_tables.index(table)]