# 4 -Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

def dec_bin(num, binary=''):
    if num != 0:
        binary += dec_bin(num//2, binary) + str(num % 2)
    return binary


num = int(input('Введите десятичное число:\n'))
try:
    if num > 0:
        binary_num = dec_bin(num)
    print(binary_num)
except:
    print('Введите положительное число')
