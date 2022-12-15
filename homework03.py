# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

count = int(input('Введите количество элементов списка: '))
# my_list = []
# for i in range(count):
#     my_list.append(random.randint(1, 999))
my_list = [random.randint(1, 999) for _ in range(count)]
print(my_list)

sum_digits = 0
for i in range(1, count, 2):
    sum_digits += my_list[i]
print(sum_digits)