# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

import random

num = [random.randint(1, 100) for i in range(200)]
print(num)

index_of_num = []
for i in range(len(num)):
    index_of_num.append(i)

cort_of_num = list(zip(index_of_num, num))
print(cort_of_num)
