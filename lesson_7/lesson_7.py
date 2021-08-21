# a = open('text.txt', 'a+', encoding='UTF-8')
# print(a.write("\n это наш гимн!"))
# a.close()

# with open('text.txt', 'r', encoding='UTF-8') as file:
#     print(file.readline())

a = open('text3.txt', 'r',  encoding='UTF-8')
print(a.read())
a.close()

