class Human:
    # Визначте для нього два статичні атрибути: default_name та default_age.
    default_name = ''
    default_age = None

    # Створіть метод __init__(), який, крім self, приймає ще два параметри: name і age.
    # Для цих параметрів вкажіть значення за замовчанням, використовуючи атрибути default_name та default_age.
    # У методі __init__() визначте чотири атрибути: Публічні - name та age. Приватні - money та house.

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    # Реалізуйте довідковий метод info(), який виводитиме поля name, age, house і money.
    def info(self):
        return f' Name {self.name},\n Age {self.age},\n Money {self.__money},\n House {self.__house} '

    # Реалізуйте довідковий статичний метод default_info(), який виводитиме статичні атрибути default_name та default_age.
    @staticmethod
    def default_info():
        return f'{Human.default_name}, {Human.default_age}'

    # Реалізуйте приватний метод make_deal(), який відповідатиме за технічну реалізацію купівлі будинку:
    # зменшувати кількість грошей на рахунку та привласнювати посилання на щойно куплений будинок.
    # Як аргументи даний метод приймає об'єкт будинку та його ціну.
    def __make_deal(self, house, price):
        if self.__money >= price:
            self.__money -= price
            self.__house = house
            print(f"Deal went successful!")
        else:
            print("Not enough money to buy this house.")

    # Реалізуйте метод earn_money(), який збільшує значення якості money.
    def earn_money(self):
        self.__money += 1000
        print(f'Now on my account {self.__money}')

    # Реалізуйте метод buy_house(), який перевірятиме, що людина має достатньо грошей для покупки, і здійснювати угоду.
    # Якщо грошей надто мало – потрібно вивести попередження в консоль.
    # Параметри методу: посилання на будинок та розмір знижки

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)

        if self.__money >= final_price:
            self.__make_deal(house, final_price)
            print(f"House was bought, congrats! On your bank account {self.__money}")
        else:
            print(f"Unfortunately, not enough money to buy this house.\n"
                  f"House price is {final_price} and your amount is {self.__money}")


class House:
    # Створіть метод __init__() і визначте всередині нього два атрибути: _area та _price.
    # Свої початкові значення вони набувають з параметрів методу __init__()

    def __init__(self, area, price):
        self._area = area
        self._price = price

    # Створіть метод final_price(), який приймає як параметр розмір знижки та повертає ціну з урахуванням даної знижки.
    def final_price(self, discount):
        self._price -= discount
        return self._price

    def __str__(self):
        return f"area {self._area}m2 and price ${self._price}"
# в мене виводився обʼєкт <__main__.SmallHouse object at 0x10296ab90> замість внятного тексту, захендлила отак


# Створіть клас SmallHouse, успадкувавши його функціонал від класу House
# Усередині класу SmallHouse перевизначте метод __init__() так, щоб він створював об'єкт із площею 40м2
class SmallHouse(House):

    def __init__(self, price):
        super().__init__(40, price)


# Викличте довідковий метод default_info() для класу Human()
Human.default_info()

# Створіть об'єкт класу Human
human = Human('Jane', 28)

# Виведіть довідкову інформацію про створений об'єкт (викличте метод info()).
print(human.info())

# Створіть об'єкт класу SmallHouse
sml_hs = SmallHouse(1000)

# Спробуйте купити створений будинок, переконайтеся в отриманні попередження.
human.buy_house(sml_hs, 20)

# Виправте фінансове становище об'єкта - викличте метод earn_money()
human.earn_money()

# Знову спробуйте купити будинок
human.buy_house(sml_hs, 0)

# Подивіться, як змінилося стан об'єкта класу Human
print(human.info())
