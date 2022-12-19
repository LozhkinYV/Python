# 4 Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def Nambers_Vallidation(str):
    try:
        int(str)
        return False
    except ValueError:
        return True

meaning = ('X (0, +∞) и Y (0, +∞)', 'X (0, -∞) и Y (0, +∞)', 'X (0, -∞) и Y (0, -∞)','X (0, +∞) и Y (0, -∞)')
quarter = input("Введите значение четверти (от 1 до 4) ")

if (Nambers_Vallidation(quarter)):
    print("Перезапустите программу и попробуйте ввести корректные данные")
elif (0<int (quarter)<5): 
        print (meaning [int (quarter) - 1])
else: 
    print("Перезапустите программу и попробуйте ввести корректные данные")
        
