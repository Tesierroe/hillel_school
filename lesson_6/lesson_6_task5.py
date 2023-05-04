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
