# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21

print('Введите координаты первой точки:\n')
num_x_1, num_y_1 = map(int, input().split(' '))

print('Введите координаты второй точки:\n')
num_x_2, num_y_2 = map(int, input().split(' '))

distance = float(((num_x_2 - num_x_1)**2 + (num_y_2 - num_y_1)**2)**0.5)
print(int(distance*100)/100)
