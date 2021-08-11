data = ["O!", 705, "Megacom", 550, "Beeline", 770]

names = []
code = []

# Пройтись по списку data, добавить имена компаний в names и коды в code 

print(names)    # ['O!', 'Megacom', 'Beeline']
print(code)     # [705, 550, 770]

# Преобразовать списки names и code в кортеж

print(type(names))  # <class 'tuple'>


# Создать словарь my_dict на основе кортежей names и codes с помощью функции zip()

print(my_dict) # {'O!': 705, 'Megacom': 550, 'Beeline': 770}

# Добавить к Ошке, Меге и Билайну коды, которые вы знаете

print(my_dict) # (пример) {'O!': [705, 703, 500], 'Megacom': [550, 999], 'Beeline': [770, 222]}
