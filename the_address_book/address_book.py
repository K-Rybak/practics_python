class address_book():
    store = {
        'name': {
            'phone': 87772009786,
            'address': 'st.Markova, d23',
            'email': 'abcde@mail.ru'
        }
    }
    def __init__(self) -> None:
        pass

    def add_contact(name, phone, address, email):
        address_book.store[name] = {
            'phone': phone,
            'address': address,
            'email': email}

    def get_contact(name):
        print(address_book.store[name])

    def get_all_contact():
        for name, address in address_book.store.items():
            print(f'Контакт {name} с адресом {address}')