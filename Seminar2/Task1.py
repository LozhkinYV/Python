# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def Nambers_Vallidation(str):
    try:
        float(str)
        return False
    except ValueError:
        return True

def Sum_Number(str):
    sum = 0
    for i in str:
        if i != ".":
            sum += int(i)
    return sum

print("Введите число")
number = input("N = ")

if Nambers_Vallidation(number):
    print("\nПерезапустите программу и попробуйте ввести корректные данные")
else:
    print(f'Сумма цифр числа {number} -> {Sum_Number(number)}')

