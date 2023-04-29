class FormulaError(Exception):
    pass


def count(formula):
    elements = formula.split()

    # 1
    if len(elements) != 3:
        raise FormulaError('Invalid formula! Try to change smth')

    # 2
    try:
        num1 = float(elements[0])
        num2 = float(elements[2])
    except ValueError:
        raise FormulaError('Invalid formula')

    # 3
    if elements[1] not in ['+', '-']:
        raise FormulaError('Invalid formula, there should be + or - operator')

    if elements[1] == '+':
        result = num1 + num2
    else:
        result = num1 - num2
    return result


formula = input('Enter a formula separated with the space: ')

try:
    result = count(formula)
    print('Your result is :', result)
except FormulaError as error:
    print('Error:', error)
