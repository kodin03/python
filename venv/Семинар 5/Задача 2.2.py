
# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import random


message = ['Ваш ход']
n = 2021
m = 28

def introduce_players():
    player1 = input('Введите Ваше имя:\n')
    player2 = 'Бот'
    print(f'Очень приятно, я {player2}')
    return [player1, player2]


def game(n, m, players, message):
    count = random.randint(0, 1)
    if n % 10 == 1 and 9 > n > 10:
        letter = 'а'
    elif 1 < n % 10 < 5 and 9 > n > 10:
        letter = 'ы'
    else:
        letter = ''
    while n > 0:
        if not count % 2:
            move = random.randint(1, m)
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {message}')
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
    return players[count % 2]


players = introduce_players()

winer = game(n, m, players, message)
if not winer:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')