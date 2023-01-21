# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def encode(text: str) -> str:
    encoded = '' 
    previous = '' 
    count = 1
    if not text: 
        return '' 
    for char in text: 
        if char != previous: 
            if previous: 
                encoded += str(count) + previous 
            count = 1 
            previous = char 
        else: 
            count += 1 
    else: 
        encoded += str(count) + previous 
    return encoded

def decode(text: str) -> str:
    decode = ''
    count = ''
    for char in text:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

print('Изначальная строка:')
my_text = 'AAAAZZZZZZZZZZZZZxxRRRRRTTTTYHHHHHHHHHHHHHHKKKKKKKK'
print(my_text)
print()
print('Сжатая строка:')
new_text = encode(my_text) 
print(new_text)
print()
print('Распакованная строка:')
my_text = decode(new_text)
print(my_text)
 