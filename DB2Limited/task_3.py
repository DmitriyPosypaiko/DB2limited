list = [
    ("Tom", "19", "167", "54"),
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75"),
    ("John", "27", "190", "87"),
    ("Jony", "24", "191", "98"),
    ]


def func():
    list.sort(key=lambda i: i[n], reverse=True)
    print(list)


if __name__ == '__main__':
    n = input('Отсортировать по имени нажмите [1], по возрасту [2], по росту [3], по весу [4]\n'
              '---> ')
    n = int(n) - 1
    func()
