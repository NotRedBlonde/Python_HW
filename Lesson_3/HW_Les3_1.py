# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

num = int(input('Введите количество элементов массива:\n'))
list_of_numbers = []
sum_list = []
sum_result = 0
try:
    if num > 0:
        for i in range(num):
            list_of_numbers.append(random.randint(0, 10))
        print(list_of_numbers)
        for position in range(0, len(list_of_numbers)):
            if position % 2 == 1:
                sum_list.append(list_of_numbers[position])
            else:
                position += 1
        sum_result = sum(sum_list)
        print(sum_result)
except:
    print('Вы ввели отрицательное число или ноль')
