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
        print(address_book.store[name])


    def get_all_contact(self):
        for name, address in address_book.store.items():
            print(f'Контакт {name} с адресом {address}')


    def save_data(self):
        f = open('address_book.data', 'wb')
        pickle.dump(address_book.store, f)
        f.close()
    
