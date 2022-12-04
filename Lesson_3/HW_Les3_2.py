# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
import random

product_of_num = []

num = int(input('Введите количество элементов массива:\n'))
list_of_numbers = []
for i in range(num):
    list_of_numbers.append(random.randint(-10, 10))
print(list_of_numbers)

for i in range(len(list_of_numbers)//2 + len(list_of_numbers) % 2):
    product_of_num.append(list_of_numbers[i]*list_of_numbers[-1 - i])
print(product_of_num)
