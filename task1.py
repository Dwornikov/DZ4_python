def push_list(a):
    my_list = [] 
    for _ in range(a):
        element = input("Введите элемент списка: ")
        my_list.append(element)
    return my_list

n = int(input('Введите количество элементов первого списка: '))
m = int(input('Введите количество элементов второго списка: '))

print('Заполнение первого списка:')
list_1 = push_list(n)

print('Заполнение второго списка:')
list_2 = push_list(m)

list_3 = []
for i in range(n):
    for j in range(m):
        if list_1[i] == list_2[j]:
            if list_1[i] not in list_3:
                list_3.append(list_1[i])

list_3.sort()

print('Общие элементы списков:', list_3)
