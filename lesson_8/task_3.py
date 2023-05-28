class Record:
    def __init__(self, name, phone_number, surname=''):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.name} {self.surname} {self.phone_number}'

    def __repr__(self):
        return str(self)


class Spravochnik:
    def __init__(self):
        self.records = [Record('Police', '911'), Record('Fire', '112'), Record('Ambulance', '666')]

    def add_record(self, name, phone_number, surname=''):
        self.records.append(Record(name, phone_number, surname))

    def remove_record(self, id):
        if 2 < id < len(self.records):
            self.records.pop(id)
        else:
            print("This number can't be removed")

    def edit_record(self, id, name, phone_number, surname=''):
        if 2 < id < len(self.records):
            self.records[id] = Record(name, phone_number, surname)
        else:
            print("This number can't be edited")

    def __str__(self):
        return '\n'.join([str(id) for id in self.records])


class Interface:

    @staticmethod
    def int_input(message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print('You should try to enter the int type')

    @staticmethod
    def string_input(message):
        return input(message)

    @staticmethod
    def get_record():
        name = Interface.string_input("Write a name: ")
        surname = Interface.string_input("Write a surname: ")
        phone_number = Interface.string_input("Write a phone: ")
        return name, phone_number, surname

    def __init__(self, spravochnik):
        self.spravochnik = spravochnik

    def start(self):
        while True:
            print("1. Add a record")
            print("2. Delete a record")
            print("3. Edit a record")
            print("4. View all records")
            print("5. Exit")

            choice = self.string_input("\nSelect the action: ")

            if choice == '1':
                name, phone_number, surname = self.get_record()
                self.spravochnik.add_record(name, phone_number, surname)

            elif choice == '2':
                id = self.int_input('Enter the record id: ')
                self.spravochnik.remove_record(id)

            elif choice == '3':
                id = self.int_input('Enter the record id: ')
                name, phone_number, surname = self.get_record()
                self.spravochnik.edit_record(id, name, phone_number, surname)

            elif choice == '4':
                print(self.spravochnik)

            elif choice == '5':
                break
            else:
                print('Invalid choice')


def main():
    spravochnik = Spravochnik()
    interface = Interface(spravochnik)
    interface.start()


if __name__ == '__main__':
    main()
