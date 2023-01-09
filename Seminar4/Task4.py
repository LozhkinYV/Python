# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0
#      или x² + 5 = 0
#      или 10*x² = 0

import random


def Random_List(namber: int) -> list[int]:
    lst = [random.randint(0, 10) for i in range(namber)]
    return lst


def Polynomial(namber: int, lst: list[int]) -> str:
    line = ''
    for i in range(namber-1):
        if (lst[i] != 0) and (lst[i] != 1):
            line += (f'{lst[i]}*{"x"}^{namber} + ')
        elif lst[i] != 0:
            line += (f'{"x"}^{namber} + ')
        namber -= 1
    if (lst[i+1] != 0) and (lst[i+1] != 1):
        line += (f'{lst[i+1]}*{"x"} + ')
    elif lst[i+1] != 0:
        line += (f'{"x"} + ')
    line = line[:-2] + (f'= 0')
    return line


k = int(input("Введите значение натуральной степени k = "))
my_list = Random_List(k)
print(my_list)

poly = Polynomial(k, my_list)
print(poly)
