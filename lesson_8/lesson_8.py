students = [
    {
        'student': 'Azat',
        'active': False,
        'course': 1
    },
    {
        'student': 'Azamat',
        'active': False,
        'course': 1
    },
    {
        'student': 'Azim',
        'active': False,
        'course': '1'
    },
]

def show_all_students(lst):
    for i in lst:
        print(i)

# show_all_students(students)

def add_student(lst):
    name = input('Enter name: ')
    course = input('Enter course')
    student = dict(student = name.title(), active = True, course = course)
    lst.append(student)
    show_all_students(lst)

# add_student(students)

def edit_student(lst):
    show_all_students(students)
    name = input('Enter name for editing: ')
    for i in lst:
        if i['student'] == name.title():
            course = input('Enter course')
            active = int(input('Enter active 0 or 1'))
            i['active'] = bool(active)
            i['course'] = course
            show_all_students(students)
# edit_student(students)


def delete_student(lst):
    show_all_students(students)
    name = input('Enter name for editing: ')
    for i in lst:
        if i['student'] == name.title():
            students.remove(i)
    show_all_students(students)

# delete_student(students)

while True:
    command = input("Enter what we'll do: add, edit or delete or 'q' for quite")
    if command == 'add':
        add_student(students)
    elif command == 'edit':
        edit_student(students)
    elif command == 'delete':
        delete_student(students)
    elif command == 'q':
        print('program stop!')
        break