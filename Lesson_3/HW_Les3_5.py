# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Решение оформлять в виде функций

fibo_list = [0]
fib_num_1 = 0
fib_num_2 = 1
neg = 1
num = int(input('Введите количество чисел:\n'))
for i in range(1, num+1):
    fib_num_1, fib_num_2 = fib_num_2, fib_num_1+fib_num_2
    fibo_list.append(fib_num_1)
    fibo_list.insert(0, neg*fib_num_1)
    neg *= -1
print(fibo_list)
