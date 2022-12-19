# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def Nambers_Vallidation(str):
    try:
        float(str)
        return False
    except ValueError:
        return True


x = input('Введите значение координаты х = ')
y = input('Введите значение координаты y = ')

if (Nambers_Vallidation(x) and Nambers_Vallidation(y)):
    print("Перезапустите программу и попробуйте ввести корректные данные")
elif float(x) > 0 and float(y) > 0:
    print("Точка находится в I четверти")
elif float(x) < 0 and float(y) > 0:
    print("Точка находится во II четверти")
elif float(x) < 0 and float(y) < 0:
    print("Точка находится в III четверти")
elif float(x) > 0 and float(y) < 0:
    print("Точка находится в IV четверти")
elif float(x) == 0 and float(y) == 0:
    print("Точка находится в начале координат")
elif float(x) == 0 and float(y) != 0:
    print("Точка находится на оси У")
elif float(x) != 0 and float(y) == 0:
    print("Точка находится на оси х")
