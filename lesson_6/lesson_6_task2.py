import math


# task 2
def square(square_side):
    perimeter = 4 * square_side
    area = square_side ** 2
    diagonal = square_side * math.sqrt(2)
    print('Perimeter, Area, Diagonal: ')
    return perimeter, area, diagonal


sides = int(input('Enter the side: '))
print(square(sides))
