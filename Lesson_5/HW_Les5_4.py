# 4-Создайте два списка — один с названиями языков программирования, другой — с их нумерацией.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая (обязательно используйте tuple unpacking) — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

from typing import List


def cortege_list_creator(lang=None,
                         numbers=None) -> List[tuple[int, str]]:
    if lang is None:
        lang = ['python', 'c#', 'c++', 'rust', 'kotlin', 'java', 'swift']
    if numbers is None:
        numbers = [1, 2, 3, 4, 5, 6, 7]
    lang = list(map(str.upper, lang))
    cortege = list(zip(numbers, lang))
    return cortege


def ord_sum(cort_item: tuple[str]) -> int:

    symbol_summary = 0
    for i in cort_item:
        symbol_summary += ord(i)
    return symbol_summary


def filter_data(data: List) -> tuple[List[tuple[int, str]], int]:

    data = [(ord_sum(data[i][1]), data[i][1]) for i in range(1, len(data))
            if not ord_sum(data[i][1]) % data[i][0]]
    elem_ord_sum = 0
    for i in data:
        elem_ord_sum += i[0]
    return data, elem_ord_sum


data_list = cortege_list_creator()
result = filter_data(data_list)
print(f'Результат: {result[0]}\nСумма чисел: {result[1]}')
