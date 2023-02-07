# # 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# #     *Пример:*
# #     - Для N = 5: 1, -3, 9, -27, 81



# import random
# num = int(input("Ведите число: "))
# a=[random.randint(-10,10) for i in range(num)]
# print (a)

# # 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# #     *Пример:*
# #     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# num = int(input("Ведите число: "))
# d = {a: 3*a+1 for a in range(1, num+1)}
# print (d)


# # 3. Напишите программу, в которой пользователь будет задавать две строки, 
# #               а программа - определять количество вхождений одной строки в другой.


# 5 Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#
# *Пример:*
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# Фибоначчи:    0,1  0,1,1  0,1,1,2   0,1,1,2,3    0,1,1,2,3,5   0,1,1,2,3,5,8   0,1,1,2,3,5,8,13   0,1,1,2,3,5,8,13,21
# число юзера:   1      2       3       4               5               6               7                   8
# для положительных: F n = F n − 1 + F n − 2
# для отрицательных: f(n)= f(n+2) - f(n+1)

# n = 3
# my_list = [0,1]
# new_list=[0]
# for i in range(1, n+1):
#     new_list.append(my_list[i-1]+my_list[i-2])
# print(new_list)




# my_dict = {1:'sdf', 
#             2: 'scvb', 
#             3: 'acvb', 
#             False: 'qweeqwr', 
#             'четыре': 'rtyiutyu',
#             (2,3,45,6,4): 'wetretyy',
#             2: 'aaaa',
#             (2,3,45,6,4): 'bbb'
            # }
# словари - набор данных, изменяемые, неупорядоченные, 
# ключи могут быть только уникальные, неизменяемые
# значения - любые

# print(my_dict)
# print(my_dict[(2,3,45,6,4)])
# print(my_dict[True])

# my_list = [[33,33], [3,64], [4,34]]
# print(dict(my_list))

# my_list = [(2,33), (3,64), (4,34)]
# print(dict(my_list))

# my_list = ((2,33), (3,64), (4,34))
# print(dict(my_list))

# my_list = ([2,33], [3,64], [4,34])
# print(dict(my_list))

# print([(i[::-1]) for i in my_list])

# print({i: i ** 3 for i in range(10)})

# my_file = open("Seminar4/sem4_Task5_1.txt", "r")
# str1 = my_file.read()
# print(str1)

# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.

# with open(r'D:\GeekBrains\5. Python\Семинар 5\New_file.txt', 'w') as f: # (r'D:\GeekBrains\5. Python\Семинар 5\New_file.txt', 'w') Это путь к папке У меня другой будет
#     f.write('1 2 3 \n4 5 6 8 \n9 10 \n')
#     f.write('77 78\n79 80 81 \n')

# path = r'D:\GeekBrains\5. Python\Семинар 5\New_file.txt'
# data = open(path, 'r')
# num_row = []
# for line in data:
#     print(line)
#     num_row += list(map(int, line.split())) # map переводит в инт формат, лист стоит чтобы создался список из строки, мап выводит строку 
# data.close()
# print(num_row)


# for i, elem in enumerate(num_row[:-1]):
#     if elem + 1 != num_row[i+1]:
#         print(elem + 1)
#         break


# 1. Дан список чисел. Создайте список, в который попадают числа,
#  описываемые возрастающую последовательность. Порядок элементов менять нельзя.
    
#     *Пример:* 
    
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.



# num_list = [1, 5, 2, 3, 4, 6, 1, 7]  
# print(num_list, end=' => ')

# min_num = num_list[0]

# for i in range(len(num_list)):
#     order_list = []
#     order_list.append(num_list[i])
#     min_num = num_list[i] 
#     for j in range(i,len(num_list)-1):
#         if num_list[j] > min_num:
#             min_num = num_list[j]
#             order_list.append(num_list[j])
#     if len(order_list) > 1:
#         print(order_list, end=' ')



# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв"

# my_str = 'АБВ ылоажы фыыдлх абв Зщышф вабвв ффлжв абВ'
# new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
# print(new_str)

import re
with open(r'Seminar7\Import_row_files.txt', 'r', encoding="utf-8") as file:
        temp = file.readlines()
print(temp)

print()
# print(len(files))
# print()

# for i in range (0, len(files), 5):
#     new_file = files.replace('\n', ', ').replace(' ', '')
#     new_pb = dict()
#     temp = re.split(":|,", new_file)
#     temp = list(temp[i] for i in range(len(temp)) if i%2)
#     new_pb[temp[2]] = {'First Name': temp[0], 'Last Name': temp[1], 'Description': temp[3]}

# print(new_pb)

files = readlines()
new_pb = dict()

for i in range(0, len(temp), 5):
    q = dict()
    q['First Name'] = temp[i].replace('\n', '').replace('First Name: ','')
    q['Last Name'] = temp[i + 1].replace('\n', '').replace('Last Name: ','')
    q['Description'] = temp[i + 3].replace('\n', '').replace('Description: ','')
    new_pb[temp[i + 2].replace('\n', '').replace('Phone Number: ','')] = q
print(new_pb)