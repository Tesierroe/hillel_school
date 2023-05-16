import json

with open('manager_sales.json') as f:
    data = json.load(f)

best_manager = None
max_sales = 0

for x in data:
    manager = x['manager']
    sales = sum(car['price'] for car in x['cars'])

    if sales > max_sales:
        best_manager = manager
        max_sales = sales


print(best_manager['first_name'], best_manager['last_name'], max_sales)


