# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]


my_list = [2, 3, 4, 5, 6]
count = 0
product_pairs = []
for i in range(len(my_list)):
    count += 1
if count % 10 == 0:
    half = count // 2
else:
    half = count // 2 + 1
index = 0
for i in my_list:

    product_pairs = [(my_list[index] * my_list[count-index-1])
                     for index in range(len(my_list)) if (count - index) >= half]
    # if count >= half:
    #     temp = my_list[index] * my_list[count - 1]
    #     product_pairs.append(temp)
    #     count -= 1
    #     index += 1
    # else:
    #     break
print(f' произведение пар = {product_pairs}')


