#1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
    # - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# num = int(input('Введите число N:\n'))
# for i in range(-num,num+1):
#     print(i)


#2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
   # *Примеры:*
    
    #- 6.78 -> 7
    #- 5 -> нет
    #- 0.34 -> 3

# num = float(input('Введите дробное число N:\n'))
# print(int(num*10)%10)


#3.Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10%.

# import random

# numbers = []
# for i in range(10):
#     numbers.append(random.randint(-100,100))
# print(numbers)

# max = numbers[0]
# for k in numbers:
#     if max < k:
#         max = k
#         print(max)

# max_10 = max*1.1
# max_09 = max*0.9

# print(max_09)
# print(max_10)
