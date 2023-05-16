import json

with open('group_people.json', 'r+') as f:
    my_data = json.load(f)

max_women_count = 0
group_id_with_max_women = None

for group in my_data:
    women_number = 0

    for person in group['people']:
        if person['gender'] == 'Female' and person['year'] > 1977:
            women_number += 1

    if women_number > max_women_count:
        max_women_count = women_number
        group_id_with_max_women = group['id_group']

print('Id of the biggest group:', group_id_with_max_women, 'Number of women: ', max_women_count)

