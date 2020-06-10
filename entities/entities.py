class Entity:
    def __init__(self, id):
        self.id = id


class Oceanarium(Entity):
    def __init__(self, id, name, establish_date, nip, owner_name, owner_last_name):
        super(Oceanarium, self).__init__(id)
        self.name = name
        self.establish_date = establish_date
        self.nip = nip
        self.owner_last_name = owner_name
        self.owner_last_name = owner_last_name


class Employee(Entity):
    def __init__(self, id, first_name, last_name, pesel, birth_date, licence_num):
        super(Employee, self).__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel
        self.birth_date = birth_date
        self.licence_num = licence_num


class Address(Entity):
    def __init__(self, id, city, postal_code, street, number, apartment_num):
        super(Address, self).__init__(id)
        self.city = city
        self.postal_code = postal_code
        self.street = street
        self.number = number
        self.apartment_num = apartment_num


class Animal(Entity):
    def __init__(self, id, name, birth_date, sex, length, weight):
        super(Animal, self).__init__(id)
        self.name = name
        self.birth_date = birth_date
        self.ex = sex
        self.length = length
        self.weight = weight


class Aquarium(Entity):
    def __init__(self, id, name, volume, water_temp, section_name):
        super(Aquarium, self).__init__(id)
        self.name = name
        self.volume = volume
        self.water_temp = water_temp
        self.section_name = section_name


class Position(Entity):

    permissions = {1: "CASHIER", 2: "TRAINER", 3: "GUIDE", 4: "ADMIN"}

    def __init__(self, id, name, description):
        super(Position, self).__init__(id)
        self.name = name
        self.description = description



