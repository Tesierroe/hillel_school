import datetime


def my_decorator(func):
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        start_time = datetime.datetime.now()
        with open('file.txt', 'a', newline='') as file:
            file.write(f"Function {func.__name__} launched at {start_time} with result {func_result} \n")
        return func_result
    return wrapper


@my_decorator
def args_sum(*args):
    summa = sum(args)
    return summa


args_sum(4, 6, 5)

