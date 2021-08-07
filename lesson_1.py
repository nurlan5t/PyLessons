# Введение в Python: Встроенные Функции, Переменные, Комментарии,
# Базовые Типы данных (Строки, Числа), Операции над ними

name = input('''Как тебя зовут? ''')
age = int(input('Сколько тебе лет? '))

print('Hello ' + name.title() + str(age))
print('Hello ', name, age)
print(f'Hello , {name}, {age}')

# age = age + 1
print(type(age))

name = 'Jack'
surname = 'Daniels'

Name = 'Jack'

a = 12
b = 5
area = a * b
print(area)

print(id(name))
print(id(Name))