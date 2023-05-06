import csv

with open('test_file.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    salaries_usd = {}
    for row in reader:
        employee = row[0]
        salaries_usd[employee] = list(map(int, row[1:]))

exchange_rate = 36.6
salaries_uah = {}
for employee, salary_usd in salaries_usd.items():
    salary_uah = [int(round(s * exchange_rate)) for s in salary_usd]
    salaries_uah[employee] = salary_uah

with open('salaries_uah.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    for employee, salary_uah in salaries_uah.items():
        writer.writerow([employee] + salary_uah)
