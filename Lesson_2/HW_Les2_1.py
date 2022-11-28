# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# (-0.56) -> 11

num = float(input('Введите дробное число:\n'))
mod_num = abs(num)
print(mod_num)
str_num = str(mod_num)
str_num = str_num.replace('.', '')
lst_str = list(str_num)
lst_num = map(int, lst_str)
s = sum(lst_num)
print(s)
