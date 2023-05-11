# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input("Введите количество элементов массива: "))
print("Поочерёдно введите элементы массива:")
list_1 = list()

for i in range(n):
    x = int(input())
    list_1.append(x)
print(list_1)

minimum = int(input("Задайте минимум: "))
maximum = int(input("Задайте максимум: "))

for i in range(len(list_1)):
    if minimum <= list_1[i] <= maximum:
        print(i, end=' ')
