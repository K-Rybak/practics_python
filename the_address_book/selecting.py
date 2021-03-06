from address_book import address_book

ab = address_book()

def user_select(select):
    if select == 1:
        ab.get_all_contact()
    elif select == 2:
        contact_name = input('Введите имя контакта\n>')
        ab.get_contact(contact_name)
    elif select == 3:
        print('Введите данные контакта\n')

        contact_name = input('Введите имя контакта\n>')
        contact_phone = input('Введите телефон контакта\n>')
        contact_address = input('Введите адрес контакта\n>')
        contact_email = input('Введите email контакта\n>')

        ab.add_contact(contact_name, contact_phone, contact_address, contact_email)
        print('\nДанные успешно добавлены!')
    elif select == 4:
        contact_name = input('Введите имя контакта\n>')
        print('Выберете, что хотите изменить:')
        print('1 - номер телефона\n2 - адрес\n3 - email\n0 - отмена\n>')

        try:
            select = int(input('> '))
            ab.change_contact(contact_name, select)
            print('Контакт успешно изменен')
        except ValueError:
            print('Введите цифру!\n')
    elif select == 5:
        contact_name = input('Введите имя контакта\n>')
        ab.delete_contact(contact_name)
        print('Контакт успешно удален')

    else:
        print('Некоректный ввод! Попробуйте снова')