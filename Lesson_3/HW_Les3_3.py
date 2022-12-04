from random import uniform
# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

num = int(input('Введите количество элементов массива:\n'))
list_of_numbers = []
for i in range(num):
    list_of_numbers.append(uniform(-10, 10))
print(list_of_numbers)
max_num = float(0)
min_num = float(1)
for i in range(len(list_of_numbers)):
    fract_num = round(list_of_numbers[i] % 1, 4)
    if fract_num >= max_num:
        max_num = fract_num
    if fract_num <= min_num:
        min_num = fract_num
print('Максимальное значение дробной части:', max_num)
print('Минимальное значение дробной части:', min_num)
result = round(max_num-min_num, 4)
print(result)
