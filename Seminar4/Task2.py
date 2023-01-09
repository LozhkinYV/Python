# 2. Напишите программу, которая составит список простых множителей числа N.

def Factor(N: int):
    my_list = []
    i = 2  # первое простое число
    while N >= i:
        if N % i == 0:
            my_list.append(i)
            N //= i
        else:
            i += 1
    return my_list


num = int(input("Введите число: "))
print(f'Для числа {num} множители -> {Factor(num)}')
