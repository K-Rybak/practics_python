from selecting import user_select
from address_book import address_book

ab = address_book()
print('''Программа адресная книга
выберете одно из действий для продолжения''')

while True:
    print('''1 - Вывести все контакты
2 - Вывести определенный контакт
3 - Добавить новый контакт
4 - Изменить контакт
5 - Удалить контакт
0 - введите для выхода''')

    try:
        select = int(input('> '))
        if select == 0:
            ab.save_data()
            print('Программа завершена!\nДо свидания!')
            break
        user_select(select)
    except ValueError:
        print('Введите цифру!\n')
        continue