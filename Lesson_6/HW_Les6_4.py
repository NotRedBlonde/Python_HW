# 4 -Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

from random import randint

num = int(input('Введите количество элементов массива:\n'))
list_of_numbers = [randint(1, 50) for i in range(num)]
print(list_of_numbers)

res_sum = []
for i in list_of_numbers:
    res_sum.append(sum(map(int, str(i))))
print(res_sum)


def filt_of_num(num: int) -> int:
    if (num % 2) == 0:
        return True
    else:
        return False


result_list = list(filter(filt_of_num, res_sum))
print(result_list)
