"""
Бригада скорой помощи выехала по вызову в один из отделенных районов. К сожалению,
когда диспетчер получил вызов, он успел записать только адрес дома и номер квартиры
K1, а затем связь прервалась. Однако он вспомнил, что по этому же адресу дома некоторое
время назад скорая помощь выезжала в квартиру K2, которая расположена в подъезде
P2 на этаже N2. Известно, что в доме M этажей и количество квартир на каждой лестничной
площадке одинаково. Напишите программу, которая вычилсяет номер подъезда P1 и номер
этажа N1 квартиры K1.

Формат ввода
Во входном файле записаны пять положительных целых чисел K1, M, K2, P2, N2. Все
числа не превосходят 106.

Формат вывода
Выведите два числа P1 и N1. Если входные данные не позволяют однозначно определить
P1 или N1, вместо соответствующего числа напечатайте 0. Если входные данные противоречивы,
напечатайте два числа –1 (минус один).

Пример 1
Ввод
Вывод
89 20 41 1 11

2 3

Пример 2
Ввод
Вывод
11 1 1 1 1

0 1

Пример 3
Ввод
Вывод
3 2 2 2 1

-1 -1
"""


def linear(a, b):
    """
    b = a * X + Y

    return X, Y
    """
    if a == 0:
        return "MANY SOLUTIONS", b
    else:
        X, Y = b // a, b % a
        return X, Y


def NOD(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n


def Diophantine(a, b, c):
    """
    c = a * X + b * Y

    return X, Y

    X, Y - Natural or 0
    a, b, c > 0

    >>> Diophantine(2, 3, 6)
    {(0, 2), (3, 0)}
    >>> Diophantine(2, 5, 1)
    set()
    """
    if c % NOD(a, b) != 0:
        return "NO SOLUTION"

    if a == 0:  # c = b * Y
        return "MANY SOLUTIONS", c // b
    elif b == 0:  # c = a * X
        return c // a, "MANY SOLUTIONS"
    else:
        answers = set()
        for x in range(0, int(c // a) + 1):
            y = (c - a * x) / b
            if y >= 0 and int(y) == y:
                answers.add((x, int(y)))

        return answers


def fun(K1, M, K2, P2, N2):
    """
    >>> fun(89, 20, 41, 1, 11)
    (2, 3)
    >>> fun(11, 1, 1, 1, 1)
    (0, 1)
    >>> fun(3, 2, 2, 2, 1)
    (-1, -1)

    K1 - квартира, для которой надо узнать подъезд P1 и этаж N1
    M - количество этажей
    K2 - квартира
    P2 - подъезд
    N2 - этаж

    X - количество квартир на каждой лестничной площадке
    Y - номер квартиры на этаже
    K = ((P - 1) * M + (N - 1)) * X + (Y + 1) (0 <= Y < X)
    K - 1 = ((P - 1) * M + (N - 1)) * X + Y
    X = ..., Y = ...
    K - Y - 1 = (P - 1) * M * X + (N - 1) * X
    """

    if N2 > M:
        return -1, -1

    X, _ = linear((P2 - 1) * M + (N2 - 1), K2 - 1)

    if X == "MANY SOLUTIONS":
        if M == 1:
            return 0, 1
        else:
            return 0, 0

    if X == 0:  # or Y == 0:
        return -1, -1

    P1, res = linear(M * X, K1 - 1)
    P1 += 1

    N1, _ = linear(X, res)
    N1 += 1

    return P1, N1

    # answers = Diophantine(M * X, X, K1 - Y - 1)

    # if answers == "NO SOLUTION":
    #     return -1, -1

    # for i in answers.copy():
    #     P1, N1 = i
    #     P1, N1 = P1 + 1, N1 + 1
    #     if N1 > M:
    #         answers.remove(i)

    # if len(answers) == 1:
    #     P1, N1 = answers.pop()
    #     return P1 + 1, N1 + 1
    # else:
    #     return -1, -1


K1, M, K2, P2, N2 = map(int, input().split())
print(*fun(K1, M, K2, P2, N2))
# print(*fun2(K1, M, K2, P2, N2))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
