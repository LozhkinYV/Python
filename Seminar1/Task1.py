# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

namber_day = input('Введите число от 1 до 7: ')
try:
    int(namber_day)
    if (0 < int(namber_day) < 6):
        print("Рабочий день")
    elif (5 < int(namber_day) < 8):
        print("Выходной день")
    else:
        print("Нет такого дня недели! Перезапустите программу и повторите ввод!")
except ValueError:
    print("Перезапустите программу и повторите ввод!")
