import Log
import View

# Сохранение в справочник
def save_data(phone: dict):
    with open('Seminar7\phonebook.txt', 'w', encoding="utf-8") as file:
        for key in phone:
            file.write(f"{key}, {phone[key]['Имя']}, {phone[key]['Фамилия']}, {phone[key]['Описание']}\n")
    
    

# Импорт такого формата: Телефон 
#                        Имя 
#                        Фамилия 
#                        Описание
def get_data_column(file_path: str):
    with open(file_path, 'r', encoding="utf-8") as file:
        phone = file.readlines()
    new_phone = dict()

    for i in range(0, len(phone), 5):
        q = dict()
        q['Имя'] = phone[i+1].replace('\n', '').replace('Имя: ','')
        q['Фамилия'] = phone[i + 2].replace('\n', '').replace('Фамилия: ','')
        q['Описание'] = phone[i + 3].replace('\n', '').replace('Описание: ','')
        new_phone[phone[i].replace('\n', '').replace('Телефон: ','')] = q
    
   
    return new_phone

# Импорт такого формата: Телефон, Имя, Фамилия, Описание
def get_data_row(file_path: str):
    with open(file_path, 'r', encoding="utf-8") as file:
        phone = file.readlines()
    new_phone = {}

    for element in phone:
        lst = element.replace('\n','').split(',')
        new_phone[lst[0]] = {'Имя': lst[1], 'Фамилия': lst[2], 'Описание': lst[3]}
    
    
    return new_phone

# Экспорт такого формата: Телефон, Имя, Фамилия, Описание
def export_row(file_path: str):
    contacts = get_data_row('Seminar7\Phonebook.txt')
    with open(file_path, 'w', encoding="utf-8") as file:
        for i in contacts:
            file.writelines(f"{i},{contacts[i]['Фамилия']},{contacts[i]['Имя']},{contacts[i]['Описание']}\n")
    


# Экспорт такого формата: Телефон 
#                         Имя 
#                         Фамилия 
#                         Описание
def export_column(file_path: str):
    contacts = get_data_row('Seminar7\Phonebook.txt')
    with open(file_path, 'w', encoding="utf-8") as file:
        for i in contacts:
            file.write(f"Номер: {i}\n")
            file.write(f"Имя: {contacts[i]['Имя']}\n")
            file.write(f"Фамилия: {contacts[i]['Фамилия']}\n")
            file.write(f"Описание: {contacts[i]['Описание']}\n")
            file.write("\n")
    


# Удаление
def deleted():
    contacts = get_data_row('Seminar7\Phonebook.txt')
    key_del = View.input_key_del()
    if key_del in contacts: del contacts[key_del]
    save_data(contacts)
    return key_del




