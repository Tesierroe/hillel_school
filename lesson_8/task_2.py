class Dot:
    def __init__(self, x, y):
        self.first = x
        self.second = y


class Triangle(Dot):
    def square(self):
        return self.first * self.second / 2


try:
    a = int(input("Enter the Base side: "))
    b = int(input("Enter the Height: "))
    tr = Triangle(a, b)
    print(f"The triangle square is {tr.square()}")
except:
    print("Base side and Height must be integers")


class Quadrate(Dot):
    def square(self):
        return self.first ** 2


try:
    a = int(input("Enter the Base side: "))
    qa = Quadrate(a, None)
    print(f"The quadrate square is {qa.square()}")
except:
    print("Base side must be integer")
