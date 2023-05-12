class Record:  # єтого достаточно чтобі обеспечить запрет на изменение этих данных другим классом ?
    def __init__(self, name, surname, phone_number):
        self._name = name
        self._surname = surname
        self._phone_number = phone_number

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_phone_number(self):
        return self._phone_number


class Spravochnik:
    def __init__(self):
        self.records = []

        self.__emergency_numbers = {
            "Police": "911",
            "Fire": "112",
            "Ambulance": "666"
        }

    def is_emergency_number(self, record):
        return record.get_phone_number() in self.__emergency_numbers.values()

    def add_record(self, record):
        self.records.append(record)

    def remove_record(self, record):
        if record in self.records and not self.is_emergency_number(record):
            self.records.remove(record)

    def edit_record(self, record, new_first_name, new_last_name, new_phone_number):
        if record in self.records and not self.is_emergency_number(record):
            record._name = new_first_name
            record._surname = new_last_name
            record._phone_number = new_phone_number

    def print_all_records(self):
        # Создаю список из записей экстренных номеров
        emergency_records = []
        for name, number in self.__emergency_numbers.items():
            emergency_records.append(Record(name, "", number))
# Объединяю список экстренных номеров и список остальных записей, но список єкстренніх номеров все равно не віводится в консоли

        all_records = emergency_records + self.records

        return all_records


class Interface:
    def __init__(self, phone_book):
        self.phone_book = phone_book

    @staticmethod
    def get_valid_input(prompt, valid_options=None):
        while True:
            user_input = input(prompt)
            if valid_options and user_input not in valid_options:
                print("Неверный ввод. Попробуйте снова что-ли")
            else:
                return user_input

    def start(self):
        while True:
            print("1. Добавить запись")
            print("2. Удалить запись")
            print("3. Редактировать запись")
            print("4. Вывести все записи")
            print("5. Выйти")

            choice = self.get_valid_input("\nВыберите действие: ", [str(i) for i in range(1, 6)])

            if choice == '1':
                self.add_record()
            elif choice == '2':
                self.remove_record()
            elif choice == '3':
                self.edit_record()
            elif choice == '4':
                self.print_all_records()
            elif choice == '5':
                break

    def add_record(self):
        print("Введите данные новой записи:")
        first_name = self.get_valid_input("Имя: ")
        last_name = self.get_valid_input("Фамилия: ")
        phone_number = self.get_valid_input("Телефон: ")
        record = Record(first_name, last_name, phone_number)
        self.phone_book.add_record(record)
        print("Запись добавлена!")

    def remove_record(self):
        print("Введите данные записи, которую нужно удалить:")
        first_name = self.get_valid_input("Имя: ")
        last_name = self.get_valid_input("Фамилия: ")
        phone_number = self.get_valid_input("Телефон: ")
        record = Record(first_name, last_name, phone_number)
        self.phone_book.remove_record(record)
        print("Запись удалена!")

    def edit_record(self):
        print("Введите данные записи, которую нужно отредактировать:")
        first_name = self.get_valid_input("Имя: ")
        last_name = self.get_valid_input("Фамилия: ")
        phone_number = self.get_valid_input("Телефон: ")
        record = Record(first_name, last_name, phone_number)

        new_first_name = self.get_valid_input("Новое имя: ")
        new_last_name = self.get_valid_input("Новая фамилия: ")
        new_phone_number = self.get_valid_input("Новый телефон: ")

        self.phone_book.edit_record(record, new_first_name, new_last_name, new_phone_number)
        print("Запись отредактирована!\n")

    def print_all_records(self):
        print("\nВсе записи в телефонной книге:")
        for record in self.phone_book.records:
            print(f"Имя: {record.get_name()}")
            print(f"Фамилия: {record.get_surname()}")
            print(f"Телефон: {record.get_phone_number()}")
            print("-" * 20)


def main():
    phone_book = Spravochnik()
    interface = Interface(phone_book)
    interface.start()


if __name__ == '__main__':
    main()
