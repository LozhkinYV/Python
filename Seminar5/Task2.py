# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random


# проверка правил User'a
def rule_check(candy: int, total: int) -> int:
    while 99999:
        num = int(input(f'Возьмите конфету от 1 до {candy}\n'))
        if total > candy:
            if num > candy:
                print(f'Можно брать не больше {candy} конфет.')
                continue
            if num < 1:
                print(f'Можно брать не меньше 1 конфеты. ')
                continue
            if 0 < num <= candy:
                return num
                break
        else:
            if num > total:
                print(f'Можно брать не больше {total} конфет.')
                continue
            if num < 1:
                print(f'Можно брать не меньше 1 конфеты. ')
                continue
            if 0 < num <= total:
                return num
                break


# логика бота
def bot_pleyer(candy: int, total: int) -> int:
    if total > candy:
        if total % (candy + 1):
            num = total % (candy + 1)
        else:
            num = random.randint(1, 28)
    else:
        num = total
    print(f'bot взял {num} конфет ')
    return num


# ход игры
def game_progress(player: str, total: int) -> int:
    print(f'Ход игрока {player}')
    if player == 'bot':
        num = bot_pleyer(max_candy, total)
    else:
        num = rule_check(max_candy, total)
    total = total - num
    return total


total = 200  # Сколько всего конфет
max_candy = 28  # максимально сколько можно взять конфет
name1 = input('Имя превого игрока?\n')

while 9999999:
    print(f'{name1}, c кем играем? ')
    player2 = int(input(
        'Выберите с кем играем. Для этого введите 1 или 2:\n 1. Игрок\n 2. bot \n'))
    if player2 == 1:
        name2 = input('Имя второго игрока? (только не "bot"!)\n')
        break
    elif player2 == 2:
        name2 = 'bot'
        break

print(f'---------------')
print(f'У нас {total} конфет')

while total > 0:
    win = name1
    total = game_progress(win, total)
    if total == 0:
        break
    print(f'---------------')
    print(f'Осталось {total} конфет')
    win = name2
    total = game_progress(win, total)
    if total == 0:
        break
    print(f'---------------')
    print(f'Осталось {total} конфет')

print(f'**************')
print('Game over!')
print(f'{win} winner')
print(f'**************')
