# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint, choice


def play_game_vs_player(n, m, players, messages):
    count = 0
    if n % 10 == 1 and 9 > n > 10:
        letter = 'а'
    elif 1 < n % 10 < 5 and 9 > n > 10:
        letter = 'ы'
    else:
        letter = ''
    while n > 0:
        print(f'{players[count%2]}, {choice(messages)}')
        move = int(input())
        if move > n or move > m:
            print(
                f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -= 1
            else:
                return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        n = n - move
        if n > 0:
            print(f'Осталось {n} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]


def introduce_players():
    player1 = input('Давайте познакомися. Как Вас зовут?\n')
    player2 = 'Робик'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]


def get_rules(players):
    n = int(100)
    m = int(20)
    first = int(input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]


def play_game_vs_bot(rules, players, messages):
    count = rules[2]
    print(count)
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = rules[0] % rules[1] + 1
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]


greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
            'Основные правила игры: '
            'Нам будет дано некоторое количество конфет, '
            'за один ход мы можем взять не более определённого количества, '
            'о котором мы с вами договоримся.'
            'Итак, начнём!')


messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


print(greeting)

pl_vs_pl = 1
Pl_vs_bot = 2
n = int(100)
print(f'Разыграем{n} конфет\n')
m = int(20)
print(f'Максимально можно брать {m} конфет за один ход\n')

choise_for_play = int(
    input('Чтобы играть против игрока нажниме 1. Против бота нажмите 2:\n'))
if choise_for_play == 1:
    player1 = input(
        'Давайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
    player2 = input('Второй игрок, и Вы представьтесь, пожалуйста\n')
    players = [player1, player2]
    winer = play_game_vs_player(n, m, players, messages)
    if not winer:
        print('У нас нет победителя.')
    else:
        print(
            f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')
else:
    players = introduce_players()
    rules = get_rules(players)
    winer = play_game_vs_bot(rules, players, messages)
    if not winer:
        print('У нас нет победителя.')
    else:
        print(
            f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')
