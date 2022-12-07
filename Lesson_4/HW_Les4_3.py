# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4
from fb_func import get_list_data

students = get_list_data('D:\Учеба\Python\Lesson_4\students.txt')

print(students)
average_rating = '5'


for i in range(len(students)):
    if average_rating in students[i]:
        students[i] = students[i].upper()
print(students)
