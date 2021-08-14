# Создайте массив состоящий из словарей с данными классов/аудиторий Гиктека
rooms = [
    {
        'class' : 2,
        'reserved' : False
    },
    {
        'class': 3,
        'reserved': False
    },
    {
        'class': 4,
        'reserved': False
    },
    {    'class': 5,
        'reserved': False
    },
]

free_rooms = []

# Напишите функцию которая принимает ранее созданный массив, фильтрирует
# полученный массив и возвращающает не менне двух элементов из массива
def check_reserve(rooms):
    for free_room in rooms:
        if free_room['reserved'] == False:
            print('Аудитория #', free_room['class'], 'свободна')
            free_rooms.append(free_room)
check_reserve(rooms)


# Напишите функцию которая принимает отфильтрованные данные, добавляет
# новое значение каждому из элементов отфильтрованных данных и возвращает
# измененные данные с добавленными значениями
def reserve_third_room(rooms):
    for room in rooms:
        if room['class'] == 3:
            room['reserved'] = True
            print("Мы заняли нашу аудиторию", room)
reserve_third_room(free_rooms)

# Напишите функцию которая принимает массив ранее измененых данных,
# меняет значение в каждом из элементов и возращает измененные данные
def leave_room(rooms):
    for room in rooms:
        if room['reserved'] == True:
            room['reserved'] = False
leave_room(free_rooms)

# Напишите функцию которая принимает массив ранее измененых данных,
# и поочередно выводит их в консоль
def show_in_console(rooms):
    for room in rooms:
        print(room)
show_in_console(free_rooms)