from address_book import address_book


print('''Программа адресная книга
выберете одно из действий для продолжения
для выхода введите 0''')

while True:
    print('''1 - Вывести все контакты
2 - Вывести определенный контакт
3 - Добавить новый контакт''')
    user_select = int(input('> '))

    if user_select == 1:
        address_book.get_all_contact()
    elif user_select == 2:
        contact_name = input('Введите имя контакта\n>')
        address_book.get_contact(contact_name)
    elif user_select == 3:
        print('Введите данные контакта')

        contact_name = input('Введите имя контакта\n>')
        contact_phone = input('Введите телефон контакта\n>')
        contact_address = input('Введите адрес контакта\n>')
        contact_email = input('Введите email контакта\n>')

        address_book.add_contact(contact_name, contact_phone, contact_address, contact_email)
        print('Данные успешно добавлены!')
    elif user_select == 0:
        print('Программа завершена!\nДо свидания')
        break