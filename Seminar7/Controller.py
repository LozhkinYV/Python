import View
import Function
import Log


def start():
    stop = False
    while stop != 4:
        option = View.input_option()

        # 1 Сохраниение
        if option == '1':
            new_phone = View.input_phone()
            Function.save_data(new_phone)
            print("Сохранено")
            Log.log('Сохранение нового абонента')

        # 2 Импорт
        elif option == '2':
            form = View.input_data_format()
            path = View.input_file_path()
                    # 1 Формат в одну строку
            if form == 1:
                new_phone = Function.get_data_row(path)
                Log.log('Импорт справочника абонентов записанных в строку')
                    # 2 Формат построчный
            elif form ==2: 
                new_phone = Function.get_data_column(path)
                Log.log('Импорт справочника абонентов записанных в колонку')
            Function.save_data(new_phone)
            print("Импортировано")
            

        # 3 Экспорт
        elif option == '3':
            form = View.input_data_format()
            path = View.input_file_path()
                    # 1 Формат в одну строку
            if form == 1:
                Function.export_row(path)
                Log.log(f'Экспорт Phonebook.txt в строку')
                    # 2 Формат построчный
            elif form ==2: 
                Function.export_column(path)
                Log.log(f'Экспорт Phonebook.txt в ряд')
            print("Экспортировано")

        # Удаление контакта
        elif option == '5':
            key_del = Function.deleted()
            Log.log(f'Удаление номера {key_del}')
            

        # 4 Выход
        else: 
            stop = 4