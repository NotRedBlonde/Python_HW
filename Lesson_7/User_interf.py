from constants import ABILITIES
from cheks import give_int

choise_action = 'Выберите действие из списка:\n'


def get_menu_item():
    """
    Функция выводит все возможные действия с БД

    Returns:
       choise: Выбор пользователя -> int
    """
    for i, item in list(enumerate(ABILITIES, start=1)):
        print(i, item, end='\n')
    choise = give_int(choise_action, 1)
    return choise


if __name__ == '__main__':
    get_menu_item()
