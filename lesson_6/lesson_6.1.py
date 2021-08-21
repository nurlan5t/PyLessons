import random
# from lesson_6 import plus
# print(plus(1, 2))

# while True:
#     request = input(''' Let's' Play? y/n' ''')
#     if request == 'y':
#         persons = int(input('How many people? '))
#         for player in range(persons):
#             first = random.randint(1, 6)
#             second = random.randint(1, 4)
#             res = first + second
#             print('{} + {}'.format(first, second))
#     elif request == 'n':
#         break

import random

number = random.randint(1, 100)
count = 5
while count != 0:
    count -= 1
    try:
        guess = int(input('Guess the number '))
    except ValueError:
        print('Вводите целые числа!')
        continue    
    if guess == number:
        print(' Yes! You guessed the number in {} attempts'.format(count))
        break
    elif guess < number:
        print(' greater ')
    elif guess > number:
        print(' less ')
    else:
        print('enter only integers')
