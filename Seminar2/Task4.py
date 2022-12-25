def Nambers_Vallidation(str):
    try:
        int(str)
        return False
    except ValueError:
        return True



print("Введите целое число ")
N = input("N = ")

print("Введите позицию числа 1")
position_N1 = input()

print("Введите позицию числа 2")
position_N2 = input()

if (Nambers_Vallidation(N) or Nambers_Vallidation(position_N1) or Nambers_Vallidation(position_N2)):
    print("\nПерезапустите программу и попробуйте ввести корректные данные")
else:
    position_N1 = int(position_N1) - 1
    position_N2 = int(position_N2) - 1
    nambers_element = list(range(-int(N), int(N)+1)) 
    print(nambers_element)
    print(f'Длина строки {len(nambers_element)}')
    
    if 0<=position_N1<=len(nambers_element) and 0<=position_N2<=len(nambers_element):
        print (f'Произведение {nambers_element[position_N1] * nambers_element[position_N2]}')
    else:
        print ("Позициии выходят за пределы количества элементов")
       

