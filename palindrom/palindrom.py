def reverse(text):
    return text[::-1]

def isPalindrom(text):
    return reverse(text) == text

def del_forbidden_signs(text):
    forbidden_signs = ' ', '!', '?', ',', '.'

    for sign in forbidden_signs:
        text = text.replace(sign, '')
    return text

string = input('Ввелите текст: ')

if isPalindrom(del_forbidden_signs(string.lower())):
    print('Да это палидром')
else:
    print('Нет, это не палидром')
