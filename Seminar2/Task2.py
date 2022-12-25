# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math


def Nambers_Vallidation(str):
    try:
        int(str)
        return False
    except ValueError:
        return True


def Work_Number(str):
    rezalt = 1
    for i in range(1, abs(int(str))+1):
        rezalt *= int(i)
    return rezalt


print("Введите число не равное 0")
number = input("N = ")

if (Nambers_Vallidation(number) or int(number) == 0):
    print("\nПерезапустите программу и попробуйте ввести корректные данные")
else:
    print(f'Произведение цифр числа {number} -> {Work_Number(number)}')
