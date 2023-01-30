def input_phone():
    number_phone = input("Номер телефона абонента: ")
    first_name = input("Имя абонента: ")
    last_name = input("Фамилия абонента: ")
    desc = input("Описание: ")
    subskriber = dict()
    subskriber[number_phone] = {'Имя': first_name, 'Фамилия': last_name, 'Описание': desc}
    return subskriber

def input_data_format():
    print('Выберите формат данных.')
    print('1. Телефон, Имя, Фамилия, Описание')
    print('2. Телефон\n   Имя\n   Фамилия\n   Описание')
    data_format = int(input('Нажмите "1" или "2": '))
    return data_format

def input_option():
    print('Выберите опции: ')
    print('1. Сохранить. \n2. Импорт \n3. Экспорт \n4. Выход \n5. Удаление номера')
    option = input('Нажмите "1", "2", "3", "4", "5": ')
    return option

def input_file_path():
    file_path = input('Введите путь к файлу. Например, (Seminar7\is_name.txt): ')
    return file_path

def input_key_del():
    key_del = input('Введите номер, который собираетесь удалить: ')
    return key_del