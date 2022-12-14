from typing import Optional


def give_int(input_string: str,
             min_num: Optional[int] = None) -> int:
    '''
    Gives integer number

    :param input_string: welcome to input
    :param min_num: minimum for number's value
    :return: int number
    '''

    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше {min_num}!')
                continue
            return num
        except ValueError:
            print("Это не число.")
