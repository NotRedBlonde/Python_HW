import random


def random_numbers(num):
    list_of_numbers = []
    """
    function to to assign a random list
    """

    for i in range(num):
        list_of_numbers.append(random.randint(0, 10))
    return list_of_numbers


def get_unique_num(numbers):
    """
    function to find unique values ​​in a list

    Returns:
        unique: list of unique numbers
    """
    unique = []
    for num in numbers:
        if num in unique:
            continue
        else:
            unique.append(num)
    return unique


def get_list_data(filename: str) -> list[str]:
    """Перевод текста из файла в список

    Args:
        filename (str): имя считываемого файла

    Returns:
        list[str]: список в который переведем файл
    """
    with open(filename, encoding='utf-8') as file:
        return file.read().split('\n')
