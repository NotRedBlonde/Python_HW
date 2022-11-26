# 4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# Пример:
# - quarter = 1 = x∈(0, ∞) u y∈(0,∞)


num_quarter = int(input('Введите номер четверти:\n'))
if num_quarter not in range(1, 5):
    print('Введено неверное число')
elif num_quarter == 1:
    print('x∈(0, ∞) u y∈(0,∞)')
elif num_quarter == 2:
    print('x∈(-∞,0) u y∈(0,∞)')
elif num_quarter == 3:
    print('x∈(-∞,0) u y∈(-∞,0)')
else:
    print('x∈(0, -∞) u y∈(-∞, 0)')
