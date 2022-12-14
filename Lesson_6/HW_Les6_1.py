# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def input_list():
    data = input('Введите значения в списке через пробел:\n').split(" ")
    return data


def input_what_search():
    data = input('Введите значения которое будем искать:\n')
    return data

# def find_value(data_list):
#     what_find = input('Кого ищем то?\n')
#     count = 0
#     for i in range(len(data_list)):
#         if what_find in data_list[i]:
#             count += 1
#             if count == 2:
#                 return f'Индекс второго вхождения - {i}, а позиция - {i + 1}'
#     else:
#         return '2 раз не приходило, а может и первого раза не было, мы не в курсе'


def find_value(data_list: list[str], search_value: str) -> int:
    indexes = [i for i, string in enumerate(
        data_list) if search_value in string]
    print(indexes)
    try:
        return indexes[1]
    except IndexError:
        return -1


elements = input_list()
search_element = input_what_search()
result = find_value(elements, search_element)
print(result)
