# 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200. Создайте список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.

import random

num = [random.randint(1, 100) for i in range(200)]
print(num)

index_of_num = []
for i in range(len(num)):
    index_of_num.append(i)

print(index_of_num)
cort_of_num = list(zip(index_of_num, num))
print(cort_of_num)
