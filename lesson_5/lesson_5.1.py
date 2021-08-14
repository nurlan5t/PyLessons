# length = 10
# width = 7
# print(length * width)

# def cube(length=3, height=7, width=2):
#     length = int(input('Enter length: '))
#     print(length * width * height)

# a = cube(2, 4)
# print(type(a))

# def cube_return(length=3, height=7, width=2):
#     length = int(input('Enter length: '))
#     return length * width * height

# # a = cube_return(2, 4)
# # print(type(a))
# # print(a)
# print(100 - cube_return(2, 2))

from lesson_5 import selection

vuz = []
sred = []

students = [
    {
        'name' : 'Azamat',
        'ort' : 200,
        'student': False
    },
    {
        'name' : 'Adilet',
        'ort' : 100,
        'student': False
    },
    {
        'name' : 'John',
        'ort' : 46,
        'student': False
    },
]

selection(students)

# def printScores(name, *args):
#     print(name, args)
#     print(sum(args))
# printScores('Azamat', 2, 4, 2)

# def printScores(name, **kwargs):
#     print(name, kwargs)
# printScores('Azamat', first=2, second=4, third=2)