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