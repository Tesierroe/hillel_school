import time
import datetime


def lets_check_the_time(func):
    def wrapper():
        start_time = datetime.datetime.now()
        result = func()
        finish_time = datetime.datetime.now()
        delta = finish_time - start_time
        print(f"Function {func.__name__} was running {delta} ")
        return result

    return wrapper


@lets_check_the_time
def music():
    time.sleep(3)
    print('Music is over!!')


music()


#####  or  #####

# def lets_check_the_time(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         finish_time = time.time()
#         delta = finish_time - start_time
#         print(f'Function {func.__name__} was running {delta}')
#     return wrapper
#
#
# @lets_check_the_time
# def music():
#     time.sleep(3)
#     print('Music is over')
#
#
# music()
