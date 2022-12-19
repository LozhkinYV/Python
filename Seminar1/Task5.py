# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


def Nambers_Vallidation(str):
    try:
        float(str)
        return False
    except ValueError:
        return True


print("Введите координаты точки А")
xA = input("xA = ")
yA = input("yA = ")
print("\nВведите координаты точки B")
xB = input("xB = ")
yB = input("yB = ")

if Nambers_Vallidation(xA) or Nambers_Vallidation(yA) or Nambers_Vallidation(xB) or Nambers_Vallidation(yB):
    print("\nПерезапустите программу и попробуйте ввести корректные данные")
else:
    distance = math.sqrt(((float(xB) - float(xA)) ** 2) +
                         ((float(yB) - float(yA))**2))
    print(f'\nРасстояние между A{xA, yA} и B{xB, yB} = {round(distance, 3) }')
