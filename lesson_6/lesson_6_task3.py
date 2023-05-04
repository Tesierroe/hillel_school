class RangeError(Exception):
    pass


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