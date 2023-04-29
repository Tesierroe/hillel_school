# task 1
word = input('Enter the word: ')
if word == word[::-1]:
    print('+')
else:
    print('-')
# task 2
text = str(input('Enter the text: '))
word = str(input('Enter the word: '))
if word in text:
    print('YES')
else:
    print('NO')
# task 3
text = input('Enter the text: ')
if text[:3] == 'abc':
    text = 'www' + text[3:]
    print(text)
else:
    text = text + 'zzz'
    print(text)


# task 4
email = input('Enter the email: ')
sign1 = '@'
sign2 = '.'
if sign1 and sign2 in email:
    print('YES')
else:
    print('NO')


# task 5
text = input('Enter the text: ').split(' ')
if len(text) < 3:
    print('Elements are less than 3, there is only ', len(text))
else:
    print(text[-3:])

#or
# text = input('Enter the text: ').split(' ')
# print('Elements are less than 3, there is only ', len(text)) if len(text) < 3 else print(text[-3:])

