# Напишите программу вычисления арифметического выражения заданного
# строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
#
# *Пример:*
#
# 2 + 2 => 4;
# 1 + 2 * 3 => 7;
# 1 - 2 * 3 => -5;

my_str = '1 + 8   * 2 - 14/ 7'
my_str = my_str.replace(' ', '')
# my_str = my_str.replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ')
# my_list = my_str.split()
my_list = list(my_str)
print(f'my_list = {my_list}')

new_list = []
list_letter_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_znak = ['+', '-']
list_prod = ['*', '/']
for i in range(len(my_list)):
    if my_list[i] in list_letter_num:
         new_list.append(int(my_list[i]))
    else:
        new_list.append(my_list[i])
print(f'new_list = {new_list}')
list_red = [new_list[0]]
for j in range(1, len(new_list)):
    if (new_list[j - 1] in list_numbers) and (new_list[j] in list_numbers):
            num = int(new_list[j - 1] * 10 + new_list[j])
            list_red.pop(j-1)
            list_red.append(int(num))
    else:
        list_red.append(new_list[j])
print(f'list_red = {list_red}')
print(*list_red, sep='')


def composition(mi_list):
    while ('*' in mi_list) or ('/' in mi_list):
        item = 0
        while item < len(mi_list):
            if mi_list[item] == '*':
                mi_list[item-1] = mi_list[item-1] * mi_list[item + 1]
                mi_list.remove(mi_list[item])
                print(f'mi_list* = {mi_list}')
                mi_list.remove(mi_list[item])
                print(f'mi_list* = {mi_list}')
            elif mi_list[item] == '/':
                mi_list[item-1] = mi_list[item-1] / mi_list[item + 1]
                mi_list.remove(mi_list[item])
                print(f'mi_list/ = {mi_list}')
                mi_list.remove(mi_list[item])
                print(f'mi_list/ = {mi_list}')

            item += 1
    return mi_list



def sum_difference(mi_list):
    while ('+' in mi_list) or ('-' in mi_list):
        item = 0
        while item < len(mi_list):
            if mi_list[item] == '+':
                mi_list[item - 1] = mi_list[item - 1] + mi_list[item + 1]
                mi_list.remove(mi_list[item])
                print(f'mi_list+ = {mi_list}')
                mi_list.remove(mi_list[item])
                print(f'mi_list+ = {mi_list}')
            elif mi_list[item] == '-':
                mi_list[item - 1] = mi_list[item - 1] - mi_list[item + 1]
                mi_list.remove(mi_list[item])
                print(f'mi_list- = {mi_list}')
                mi_list.remove(mi_list[item])
                print(f'mi_list- = {mi_list}')

            item += 1
    return mi_list

result = composition(list_red)
result = sum_difference(list_red)
print(f'list_red = {list_red}')
print(*result)


