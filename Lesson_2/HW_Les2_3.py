import random
# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

N = int(input('Введите количество элементов массива:\n'))

list_1 = []

for i in range(N):
    list_1.append(random.randint(-100, 100))
print(list_1)
for k, item in enumerate(list_1):
    if item < 0:
        list_1.insert(k+1, 0)
print(list_1)
