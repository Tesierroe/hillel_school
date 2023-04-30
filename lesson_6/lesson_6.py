import math


# task 1
def primer(n):
    while n >= 2:
        n = n / 2
    if 1 == n:
        print("YES")
    else:
        print("NO")
    return n, 'Operation is finished'


n = int(input('Enter the number: '))
print(primer(n))


# task 2
def square(square_side):
    perimeter = 4 * square_side
    area = square_side ** 2
    diagonal = square_side * math.sqrt(2)
    print('Perimeter, Area, Diagonal: ')
    return perimeter, area, diagonal


square_side = int(input('Enter the side: '))
print(square(square_side))
