# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

product_of_num = []

num = int(input('Введите количество элементов массива:\n'))
list_of_numbers = [random.randint(-10, 10) for i in range(num)]
print(list_of_numbers)

# for i in range(len(list_of_numbers)//2 + len(list_of_numbers) % 2):
#     product_of_num.append(list_of_numbers[i]*list_of_numbers[-1 - i])
# print(product_of_num)

product_of_num = [list_of_numbers[i]*list_of_numbers[-1 - i]
                  for i in range(len(list_of_numbers)//2 + len(list_of_numbers) % 2)]

print(product_of_num)
