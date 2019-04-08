import re


def func(text):
    if text.isalpha():
        result = ''.join([i for i in text if not i.isdigit()])
        print('Букв -> ', len(''.join(c for c in result if c not in '?:!/; ')))
    elif text.isdigit():
        x = re.findall('(\d+)', text)
        print('Цифр -> ', len(x[0]))
    elif text.isalnum():
        result = ''.join([i for i in text if not i.isdigit()])
        print('Букв -> ', len(''.join(c for c in result if c not in '?:!/; ')))
        x = re.findall('(\d+)', text)
        print('Цифр -> ', len(x[0]))


if __name__ == '__main__':
    func(input('Введите предложение -> '))


