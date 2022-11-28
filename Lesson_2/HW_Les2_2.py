# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)
def fact(num):
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result


N = abs(int(input('Введите число N:\n')))
list_1 = []
for i in range(1, N+1):
    list_1.append(fact(i))
print(list_1)
