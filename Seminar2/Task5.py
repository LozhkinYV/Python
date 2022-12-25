# 5 Реализуйте алгоритм перемешивания списка.

import random 

def Nambers_Vallidation(str):
    try:
        int(str)
        return False
    except ValueError:
        return True

print("Введите целое число > 0 ")
N = input("N = ")
if Nambers_Vallidation(N) or int(N)<=0:
    print("Перезапустите программу и попробуйте ввести корректные данные")
else:
    old = list(range(int(N)))
    print(old)
    new = random.sample(old, len(old))
    print(new)