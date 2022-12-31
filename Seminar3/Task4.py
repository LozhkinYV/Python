# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import math
namber_dec = int(input("Введите целое число -> "))

# Выриант1
print (str(bin(namber_dec)).split('b')[1])

print ()
# Выриант2

namber_bin=''
while namber_dec > 0:
    namber_bin = str(namber_dec % 2) + namber_bin
    namber_dec = namber_dec // 2
 
print(namber_bin)