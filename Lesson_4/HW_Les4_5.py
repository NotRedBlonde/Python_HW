# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol
from fb_func import get_list_data


def rle_encode(data: str):
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def rle_decode(data: str):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)  # знаю что тут ошибка
            count = ''
        return decode


data_for_coding = get_list_data('D:\Учеба\Python\Lesson_4\data_for_coding.txt')
print(data_for_coding)
data_for_coding = rle_encode(data_for_coding)
print(data_for_coding)


data_for_decoding = get_list_data(
    'D:\Учеба\Python\Lesson_4\data_for_encod.txt')
print(data_for_decoding)
data_for_decoding = rle_decode(data_for_decoding)
print(data_for_decoding)
