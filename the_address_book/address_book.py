import email
import pickle

class address_book():
    store = {}

    def __init__(self):
        f = open('address_book.data', 'rb')
        address_book.store = pickle.load(f)
        f.close()

    def add_contact(self, name, phone, address, email):
        address_book.store[name] = {
            'phone': phone,
            'address': address,
            'email': email}


    def get_contact(self, name):
        for key in address_book.store[name]:
            print(f'{key}:{address_book.store[name][key]}')


    def get_all_contact(self):
        for name, data in address_book.store.items():
            print(f'Контакт {name}, данные:')
            for key, val in data.items():
                print(f'{key}:{val}')


    def change_contact(self, name, select):
        if select == 1:
            print('Введите новый номер')
            phone = input('> ')
            address_book.store[name]['phone'] = phone
        elif select == 2:
            print('Введите новый адрес')
            address = input('> ')
            address_book.store[name]['address'] = address
        elif select == 3:
            print('Введите новый адрес почты')
            email = input('> ')
            address_book.store[name]['email'] = email


    def delete_contact(self, name):
        del address_book.store[name]

    def save_data(self):
        f = open('address_book.data', 'wb')
        pickle.dump(address_book.store, f)
        f.close()
    
