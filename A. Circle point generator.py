"""
https://yandex.ru/yaintern/ml
https://contest.yandex.ru/contest/28413/enter

Петя написал два генератора точек в круге:
def generate1():
    a = uniform(0, 1)
    b = uniform(0, 1)
    return (a * cos(2 * pi * b), a * sin(2 * pi * b))
def generate2():
    while True:
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return (x, y)
Даны 100 наборов по 1000 точек, каждый набор сгенерирован каким-то одним из этих
двух алгоритмов. Необходимо определить для каждого набора, первый или второй алгоритм
использовался для его генерации.
Для того, чтобы получить ОК по этой задаче, надо предсказать правильный генератор
хотя бы для 98 наборов.

Формат ввода
Даны 100 строк. Каждая строка отвечает за свой набор точек.
В каждой строке находится 2000 действительных чисел (−1≤ai≤1−1≤ai​≤1), разделённых
пробелом. Точки идут подряд, то есть формат строки: x0x0​ y0y0​ x1x1​ y1y1​ x2x2​
y2y2​ ... x999x999​ y999y999​

Формат вывода
Нужно вывести 100 строк, в каждой из которой должно быть 1 число: 1 или 2, в зависимости
от того, первым или вторым генератором был сгенерирован данный набор точек.
"""


def generate1():
    import numpy as np

    a = np.random.uniform(0, 1)
    b = np.random.uniform(0, 1)
    return (a * np.cos(2 * np.pi * b), a * np.sin(2 * np.pi * b))


def generate2():
    import numpy as np

    while True:
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x**2 + y**2 > 1:
            continue
        return (x, y)


def gen_dots(type, lenght=1000):
    fun = generate1 if type == 1 else generate2

    text = []
    for _ in range(lenght):
        text += list(map(str, fun()))

    text = " ".join(text)
    return text


def write_dots(type, lines=100):

    l = []
    for _ in range(lines):
        l.append(gen_dots(type))

    text = "\n".join(l)
    with open("input.txt", "w") as fp:
        fp.write(text)


def what_gen(l):
    N = len(l)
    E = sum(l) / N
    D1 = 1 / 6
    D2 = 1 / 4

    for i in range(N):
        l[i] = (l[i] - E) ** 2

    D = sum(l) / (N - 1)
    print(D)
    dist1 = abs(D - D1)
    dist2 = abs(D - D2)
    return 1 if dist1 < dist2 else 2


# T = 1
# write_dots(T)

for i in range(100):

    print(what_gen(list(map(float, input().split()))))

    # ans = what_gen(list(map(float, input().split())))
    # if ans != T:
    #     print(f"{i}!!!!")
