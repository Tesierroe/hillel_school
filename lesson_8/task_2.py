class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, d1, d2, d3):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3

    def square(self):
        a = (
            self.d1.x * (self.d2.y - self.d3.y) +
            self.d2.x * (self.d3.y - self.d1.y) +
            self.d3.x * (self.d1.y - self.d2.y)
        ) / 2

        if a < 0:
            print("The coordinates for the triangle are wrong!")
            return None
        else:
            return abs(a)


class Quadrilateral:
    def __init__(self, d1, d2, d3, d4):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4

    def square(self):
        side1 = ((self.d2.x - self.d1.x) ** 2 + (self.d2.y - self.d1.y) ** 2) ** 0.5
        side2 = ((self.d3.x - self.d2.x) ** 2 + (self.d3.y - self.d2.y) ** 2) ** 0.5
        side3 = ((self.d4.x - self.d3.x) ** 2 + (self.d4.y - self.d3.y) ** 2) ** 0.5
        side4 = ((self.d1.x - self.d4.x) ** 2 + (self.d1.y - self.d4.y) ** 2) ** 0.5

        if side1 != side2 or side2 != side3 or side3 != side4:
            print("The coordinates for the quadrilateral are wrong!")
            return None
        else:
            return side1 ** 2


def get_valid_coordinates(message):
    while True:
        try:
            x = float(input(message + " Enter the x-coordinate: "))
            y = float(input(message + " Enter the y-coordinate: "))
            return x, y
        except ValueError:
            print("Please enter numeric values.")


d1_x, d1_y = get_valid_coordinates("Enter the first coordinate for dot 1:")
d1 = Dot(d1_x, d1_y)

d2_x, d2_y = get_valid_coordinates("Enter the first coordinate for dot 2:")
d2 = Dot(d2_x, d2_y)

d3_x, d3_y = get_valid_coordinates("Enter the first coordinate for dot 3:")
d3 = Dot(d3_x, d3_y)

tr = Triangle(d1, d2, d3)
triangle_area = tr.square()
if triangle_area is not None:
    print(f"The triangle square is {triangle_area}")

d4_x, d4_y = get_valid_coordinates("Enter the first coordinate for dot 4:")
d4 = Dot(d4_x, d4_y)

qa = Quadrilateral(d1, d2, d3, d4)
quadrate_area = qa.square()
if quadrate_area is not None:
    print(f"The quadrilateral square is {quadrate_area}")
