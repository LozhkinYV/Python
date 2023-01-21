# 3. Создайте программу для игры в ""Крестики-нолики"".


import os


def field(lst: list) -> list:
    os.system('cls||clear')
    count = 0
    print(f'-------------')
    for i in range(3):
        print(f'| {lst[(count)]} | {lst[count+1]} | {lst[count+2]} |')
        print(f'-------------')
        count += 3


def game_over(lst: list, num: int) -> int:
    if (lst[0] == lst[1] == lst[2]
        or lst[3] == lst[4] == lst[5]
        or lst[6] == lst[7] == lst[8]
        or lst[0] == lst[4] == lst[8]
        or lst[2] == lst[4] == lst[6]
        or lst[0] == lst[3] == lst[6]
        or lst[1] == lst[4] == lst[7]
            or lst[2] == lst[5] == lst[8]):
        return 1
    elif num == 9:
        return 2
    else:
        return 3


def game_progress(st: str, lst: list) -> list:
    while 999999:
        position = int(input(f'Куда поставим {st}: '))
        if 0 < position < 10:
            if lst[position-1] not in 'X0':
                lst[position-1] = st
                break
            else:
                print('Эта позиция уже занята')
                continue
        else:
            print('Такой позиции нет')


list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
move = 0
while 999999:
    field(list1)
    simbol = 'X'
    game_progress(simbol, list1)
    move += 1
    validation = game_over(list1, move)
    if validation == 1 or validation == 2:
        break
    field(list1)
    simbol = '0'
    game_progress(simbol, list1)
    move += 1
    validation = game_over(list1, move)
    if validation == 1 or validation == 2:
        break
field(list1)
print('************')
print('Game over!')
if validation == 1:
    print(f'winner {simbol}')
else:
    print('no winner')
