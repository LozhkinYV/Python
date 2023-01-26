# filter(lambda)
# 3. Задайте последовательность чисел. Напишите программу,
#           которая выведет список неповторяющихся элементов исходной последовательности.

import random


def Random_List(namber: int) -> list[int]:
    lst = [random.randint(1, 10) for i in range(namber)]
    return lst


def In_List(lst: list[int]) -> list[int]:
    new_lst = [0]
    new_lst[0] = lst[0]
    for i in range(len(lst)):
        if lst[i] not in new_lst:
            new_lst.append(lst[i])
    return new_lst


my_list = Random_List(10)
print(f'Рандомный список -> {my_list}')
new_list1 = In_List(my_list)
print(f'Новый список без повторений -> {new_list1}')

new_list2 = list(filter(lambda x: not my_list.count(x)>1, my_list))
print(f'Cписок уникальных значений -> {new_list2}')