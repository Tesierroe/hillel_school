# task 6
def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))


number1 = int(input('Enter the 1st number: '))
number2 = int(input('Enter the 2nd number: '))
print(sum_range(start=number1, end=number2))
