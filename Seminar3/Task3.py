# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random


def Random_List(namber: int):
    lst = [round(random.uniform(1, 10), 2) for i in range(namber)]
    return lst


num = int(input("Какое количество чисел будет в списке? -> "))
my_list = Random_List(num)
print(my_list)

new_list = [round(i % 1, 2) for i in my_list if i % 1 != 0]

print(new_list)  # вывод дробной части

print(max(new_list) - min(new_list))
