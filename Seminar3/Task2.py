# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16]
# - [2, 3, 5, 6] => [12, 15]

import random

def Random_List(namber: int):
    lst = [random.randint(1, 10) for i in range(namber)]
    return lst

num = int(input("Какое количество чисел будет в списке? -> "))
my_list = Random_List(num)
print(my_list)


new_list = []
for i in range((len(my_list)+1)//2):
    new_list.append(my_list[i]*my_list[-i-1])
print(f'Произведение пар чисел списка {new_list}')
