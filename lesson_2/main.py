# task 1
celsius = int(input("Enter the C temperature "))
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.16
print(f"It's {fahrenheit} in Fahrenheits and {kelvin} in Kelvins")
# начебто формула переводу С в F така (25 °C × 9/5) + 32 = 77 °F

# task 2
v1 = int(input("Enter the v1 volume "))
t1 = int(input("Enter the t1 temperature "))
v2 = int(input("Enter the v2 volume "))
t2 = int(input("Enter the t2 temperature "))
vol_and_temp = int(v1*t1 + v2*t2) / (v1 + v2)
print(f'The volume and temperature of the mixture: {vol_and_temp}')

# task 3
cur1 = input('From currency: ')
cur2 = input('To currency: ')
amount = int(input('Enter the amount: '))

if cur1 == 'USD' and cur2 == 'UAH':
    print(amount * 36.7, 'UAH')
elif cur1 == 'UAH' and cur2 == 'USD':
    print(amount / 0.027, 'USD')
elif cur1 == 'EUR' and cur2 == 'UAH':
    print(amount * 40.31, 'UAH')
elif cur1 == 'UAH' and cur2 == 'EUR':
    print(amount / 0.025, 'EUR')
else:
    print('Check the correctness of currency name')

# task 4
num1 = float(input('Enter 1st number: '))
num2 = float(input("Enter 2nd number: "))
op = input("Enter the operation (+, -, *, /): ")
# r = None

if op == '+':
    r = num1 + num2
elif op == '-':
    r = num1 - num2
elif op == '*':
    r = num1 * num2
elif op == '/':
    r = num1 / num2
else:
    print("Check the correctness of operation name")

print(f'Result is {r}')
