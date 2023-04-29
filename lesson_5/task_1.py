import math


class DiscriminantError(Exception):
    pass


a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    raise DiscriminantError("Discriminant is negative.")
else:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Roots are: x1 =", x1, ", x2 =", x2)
