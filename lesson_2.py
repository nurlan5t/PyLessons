# Условные конструкции и Операторы сравнения, Циклы

svetofor = 'off'
if svetofor == 'green':
    print('Go')
elif svetofor == 'yellow' or 'red':
    print('stop')
else:
    'look at situation'


number = 100
guess = int(input('введите число: '))

if number != guess:
    print('не равно')
# if number >= guess:
#     print('больше')
elif number == guess:
    print('равно')
else:
    print('введите правильное число')

# ==, <=, >=, !=