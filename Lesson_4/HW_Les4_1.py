# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]
from fb_func import get_unique_num
N = abs(int(input('Введите натуральное число:\n')))
prime_factors_list = []


def prime_factors(num: int) -> int:
    """function to find all prime factors

    Args:
        num (int): our number, that we need to find prime factors

    Returns:
       result_list: list of all prime numbers of our number
    """
    result_list = []
    d = 2
    while d * d <= num:
        if num % d == 0:
            result_list.append(d)
            num //= d
        else:
            d += 1
    if num > 1:
        result_list.append(num)
    return result_list


prime_factors_list = list(prime_factors(N))
print(prime_factors_list)

result_fact_list = get_unique_num(prime_factors_list)
print(result_fact_list)
