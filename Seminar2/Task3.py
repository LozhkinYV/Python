# 3 Задайте список из n чисел, заполненных по формуле (1+1/n)**n и выведите на экран их сумму.

# *Пример:*
# - Для n = 6: [2,2,2,2,2,3] -> 13

import math


def Nambers_Vallidation(str):
    try:
        int(str)
        return False
    except ValueError:
        return True


def Sum_Number(str):
    n = abs(int(str))
    resalt = [round((1+1/i)**i) for i in range(1, n+1)]
    return resalt

print("Введите число не равное 0")
number = input("N = ")

if (Nambers_Vallidation(number) or int(number) == 0):
    print("\nПерезапустите программу и попробуйте ввести корректные данные")
else:
    print(f'Для N = {number}: {Sum_Number(number)} -> {sum(Sum_Number(number))}')
