import math
class RangeError(Exception):
    pass


# task 1
def primer(n):
    while n >= 2:
        n = n / 2
    if 1 == n:
        print("YES")
    else:
        print("NO")
    return n, 'Operation is finished'


result = int(input('Enter the number: '))
print(primer(result))


# task 2
def square(square_side):
    perimeter = 4 * square_side
    area = square_side ** 2
    diagonal = square_side * math.sqrt(2)
    print('Perimeter, Area, Diagonal: ')
    return perimeter, area, diagonal


sides = int(input('Enter the side: '))
print(square(sides))


# task 3
def is_prime(a):
    if a not in range(2, 1000):
        raise RangeError("The number should be > 2 and < 1000.")
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
    return True


my_result = int(input("Enter a number which is > than 2: "))
print(is_prime(my_result))


# task 4
def change_list(some_list):
    if len(some_list) < 2:
        return "There should be mothe than 2 elements"
    first = some_list[0]
    last = some_list[-1]

    some_list[0] = last
    some_list[-1] = first
    return some_list


ma_list = list(input('Enter some list here: '))
new = change_list(ma_list)
print(new)


# task 5
def to_dict(lst):
    return {item: item for item in lst}


some_list = list(input("Enter the future dict : "))
my_dict = to_dict(some_list)
print(my_dict)


# не змогла зрозуміти як зробити щоб не кожний елемент списку був ключ-значення, а вони розділялися комою, типу:
# є лист [11, «Jane», 77, True] -> результатом є словник {11: 11, «Jane»: «Jane», 77: 77, True: True}
# намагалася якость через dict.fromkeys, але не докрутила. Що тут можна використати щоб отримати вірній формат словнику?

# def to_dict(lst):
#     result_dict = dict.fromkeys(lst, None)
#     for key in result_dict:
#         result_dict[key] = key
#     return result_dict
#
#
# some_list = list(input("enter the list: "))
# my_dict = to_dict(some_list)
# print(my_dict)


# task 6
def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))


number1 = int(input('Enter the 1st number: '))
number2 = int(input('Enter the 2nd number: '))
print(sum_range(start=number1, end=number2))
