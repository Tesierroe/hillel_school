# task 1
def primer(n):
    while n >= 2:
        n = n / 2
    if 1 == n:
        print("YES")
    else:
        print("NO")
    return n, 'Operation is finished'


result = int(input('Enter the number: '))
print(primer(result))