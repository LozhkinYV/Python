# enumerate,  list comprehension.
# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

num = int(input("Какое количество чисел будет в списке? -> "))

def Random_List(namber: int):
    lst = [random.randint(1,10) for i in range(namber)]
    return lst

my_list = Random_List(num)
print (my_list)

# 1-й вариант
summ = 0
for i in range(len(my_list)):
    if (i%2!=0):
        summ += int(my_list[i])
print (f'Сумма элементов списка, стоящих на нечётной позиции {summ}')

# 2-й вариант
new_list = [my_list[x] for x in range(len(my_list)) if x % 2]
print(f'Сумма элементов списка, стоящих на нечётной позиции {sum(new_list)}')

# 3-й вариант
second_list= [el for i, el in enumerate(my_list, 1) if not i % 2] 
print(f'Сумма элементов списка, стоящих на нечётной позиции {sum(second_list)}')