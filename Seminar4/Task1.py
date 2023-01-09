# 1. Вычислить число c заданной точностью d.
# Пример:
# при d = 0.001,π = 3.141    10^(-1)≤d≤10^(-10).

from math import pi


def rounding(str):
    if '.' in str:
        return int((len(d) - d.find('.') - 1))
    else:
        return 0


d = input("Введите точность числа Пи от 0.1 до 0.0000000001: ")
r = rounding(d)
if 0.0000000001 <= float(d) <= 0.1:
    print(f'число Пи с заданной точностью {d} равно {round(pi, r)}')
elif float(d) == 0:
    print(f'число Пи с заданной точностью {d} равно {round(pi)}')
else:
    print('Повторите ввод')
