def reverse(text):
    return text[::-1]

def isPalindrom(text):
    return reverse(text) == text

string = input('Ввелите текст: ')

if isPalindrom(string):
    print('Да это палидром')
else:
    print('Нет, это не палидром')
