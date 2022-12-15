# Дана последовательность чисел. Получить список уникальных элементов
# заданной последовательности.
#
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
my_list = sorted(my_list)
print(f'my_list = {my_list}')
temp = my_list[0]
unnecessary_list = []
temp_list = []
unique_list = []
count = 0
for i in range(1, len(my_list)):
    if my_list[i] == temp:
        unnecessary_list.append(my_list[i])
    else:
        temp_list.append(my_list[i])
    temp = my_list[i]
    # print(f'unnecessary_list = {unnecessary_list}')
    # print(f'temp_list = {temp_list}')
for j in range(len(temp_list)):
    if temp_list[j] not in unnecessary_list:
        unique_list.append(temp_list[j])
print(f'unique_list = {unique_list}')

# решение через словарь

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
my_dict = {}
new_list = []

for item in my_list:
    my_dict[item] = my_dict.get(item, 0) + 1

for key, value in my_dict.items():
    if value == 1:
        new_list.append(key)

print(my_list)
print(my_dict)
print(new_list)
