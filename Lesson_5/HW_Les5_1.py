# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

my_text = input('Введите строку из которой будем удалять:\n')


def del_some_words(my_text: str):
    for_del = input('Введите строку для удаления:\n')
    my_text = list(filter(lambda x: for_del not in x, my_text.split()))
    return " ".join(my_text)


my_text = del_some_words(my_text)
print(my_text)
