# task 1
my_list = ["john", "marta", "james", "amanda", "marianna"]
for i in my_list:
    print(i.capitalize())

# task 2
friends = ["John", "Marta", "James", "Amanda", "Marianna"]
print('NAME'.center(10, '*'))
for name in friends:
    print(f"{name:>10}")

# or

friends = ["John", "Marta", "James", "Amanda", "Marianna"]
max_length = max(len(name) for name in friends)
print('NAME'.center(max_length, '*'))
for name in friends:
    print(name.rjust(max_length))

# task 3
my_list = ["FirstItem", "FriendsList", "MyTuple"]
for variable in my_list:
    for x in variable:
        if x.isupper():
            my_list = variable[0].lower() + variable[1:].replace(x, "_" + x.lower())
        else:
            continue
    print(my_list)


# task 4
my_dict = {'Java': 'Joe', 'Python': 'Lisa', 'C#': 'Mike', 'C++': 'Anna'}
for k,v in my_dict.items():
    print(f'My favorite programming language is {k}. It was created by {v}')
my_dict.pop('Java')
print(my_dict)


# task 5
e2g = {'stork': 'storch', 'hawk': 'falke', 'woodpecker': 'specht', 'owl': 'eule'}
print(e2g.get('owl'))

vocabulary2 = {'bla': 'ble', 'mother': 'mutter'}
e2g.update(vocabulary2)
print(f'{e2g} \n{list(e2g.items())}')


# task 6
subjects = {
    'science': {'physics': ['nuclear physics', 'optics', 'thermodynamics'],'computer science': {},'biology': {}},
    'humanities': {},
    'public': {}
}
print(list(subjects['science'].keys()))
print(subjects['science']['physics'])


# task 7
new_dict = {}
for i in range(1, 16):
    keys = i
    values = keys ** 2
    new_dict[i] = values
print(new_dict)
