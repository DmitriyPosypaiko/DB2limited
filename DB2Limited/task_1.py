def func():

    for i in range(a, b+1):
        if i % c == 0:
            X.append(i)


if __name__ == '__main__':
    X = []
    a = int(input('Введите первое число -> '))
    b = int(input('Введите второе число -> '))
    c = int(input('Введите третье число -> '))
    func()
    val = ','.join(map(str, X))
    print(f"{len(X)} потому что {val} делятся на {c}.")

