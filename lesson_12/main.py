import argparse
import math


def rivnyannya(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


def main():
    parser = argparse.ArgumentParser(description='Це квадратне рівняння, внизу приведено коєфіцієнти')

    parser.add_argument('-a', type=float, default=0, help='Коефіцієнт a')
    parser.add_argument('-b', type=float, required=True, help='Коефіцієнт b')
    parser.add_argument('-c', type=float, required=True, help='Коефіцієнт c')

    args = parser.parse_args()

    a = args.a
    b = args.b
    c = args.c
    solution = rivnyannya(a, b, c)

    if solution is None:
        print('Рівняння не має розв\'язків')
    elif isinstance(solution, float):
        print('Один корінь:')
        print(f'x = {solution}')
    else:
        print('Два корені:')
        print(f'x1 = {solution[0]}')
        print(f'x2 = {solution[1]}')


if __name__ == '__main__':
    main()
