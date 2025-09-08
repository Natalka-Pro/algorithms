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
    0 <= Y <= X - 1
    return X, Y
    """
    if a == 0:
        return "MANY SOLUTIONS", b
    else:
        # X, Y = b // a, b % a
        # return X, Y
        ans = []
        min_X = b // (a + 1)
        max_X = b // a

        for x in range(min_X, max_X + 1):
            y = b - a * x
            if 0 <= y <= x - 1:
                ans.append((x, y))

        return ans


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
    >>> fun(5, 2, 4, 1, 2)
    (0, 0)

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

    ans = linear((P2 - 1) * M + (N2 - 1), K2 - 1)

    if len(ans) == 0:
        return -1, -1

    if ans[0] == "MANY SOLUTIONS":  # P2 = 1, N2 = 1
        N1 = P1 = 0

        if M == 1:  # если всего один этаж
            N1 = 1

        if K1 <= K2:  # если неизвестная квартира до известной
            N1 = P1 = 1

        if K1 <= M:  # на этаже как минимум одна квартира => подъезд точно первый
            P1 = 1

        return P1, N1

    pos_X = [i[0] for i in ans]

    pos_P1, pos_N1 = set(), set()

    for x in pos_X:
        P1, res = (K1 - 1) // (M * x), (K1 - 1) % (M * x)
        P1 += 1

        N1 = res // x
        N1 += 1

        pos_P1.add(P1)
        pos_N1.add(N1)

    if len(pos_P1) > 1:
        P1 = 0
    else:
        P1 = pos_P1.pop()

    if len(pos_N1) > 1:
        N1 = 0
    else:
        N1 = pos_N1.pop()

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


def fun2(K1, M, K2, P2, N2):

    def trivial_cases(flat, storeys, flat_train, entrance_train, floor_train):

        if storeys < floor_train:

            # этажность меньше исследуемого(кв2) этажа

            return -1, -1

        if flat_train < (storeys * (entrance_train - 1) + floor_train):

            # кв2 меньше минимально возможного значения на `floor_train`(на каждом этаже минимум одна квартира)

            return -1, -1

        if entrance_train == 1 and floor_train == 1:

            # кв2 расположена в 1-ом подъезде и на 1-ом этаже.

            if flat <= flat_train:

                # исследуемая квартира расположена до кв2.

                return 1, 1

            if flat <= storeys:  # flat > 1, storeys > 1

                # квартира расположена в 1-ом подъезде(на каждом этаже минимум одна квартира)

                return 1, 0

            if storeys == 1:

                # этажность=1

                return 0, 1

            # больше ничего не сможем определить(если кв2 в 1 подъезде, на 1 этаже).

            return 0, 0

        # в противном случае возвращаем `False` и продолжаем поиск нетривиальных случаев.

        return False

    def get_entrance_and_floor(flats_per_floor):

        entrance = flat // (storeys * flats_per_floor) + int(
            flat % (storeys * flats_per_floor) != 0
        )

        floor = (
            flat - storeys * flats_per_floor * (entrance - 1)
        ) // flats_per_floor + int(
            (flat - storeys * flats_per_floor * (entrance - 1)) % flats_per_floor != 0
        )

        return entrance, floor

    def main_deсision(flat, storeys, flat_train, entrance_train, floor_train):

        flats_per_floor_min = flat_train // (
            storeys * (entrance_train - 1) + floor_train
        ) + int(flat_train % (storeys * (entrance_train - 1) + floor_train) != 0)

        flats_per_floor_max = (flat_train - 1) // (
            storeys * (entrance_train - 1) + floor_train - 1
        )

        if (
            (flats_per_floor_min > flats_per_floor_max)
            or (flats_per_floor_min < 1)
            or (flats_per_floor_max > 1000000)
        ):
            # не знаю почему, но на всякий - добавил flats_per_floor_max > 1000000

            return -1, -1

        entrance_main, floor_main = get_entrance_and_floor(flats_per_floor_min)

        for flats in range(flats_per_floor_min + 1, flats_per_floor_max + 1):

            entrance, floor = get_entrance_and_floor(flats)

            if entrance != entrance_main:

                entrance_main = 0

            if floor != floor_main:

                floor_main = 0

            if entrance_main == 0 and floor_main == 0:

                break

        if flat <= storeys and entrance_main != 1:

            # если `flat' в 1-ом подъезде и `entrance_main` рассчиталось неверно

            entrance_main = 1

        return entrance_main, floor_main

    flat, storeys, flat_train, entrance_train, floor_train = K1, M, K2, P2, N2

    trivial_deсision = trivial_cases(
        flat, storeys, flat_train, entrance_train, floor_train
    )

    if trivial_deсision:
        return trivial_deсision

    else:

        return main_deсision(flat, storeys, flat_train, entrance_train, floor_train)


K1, M, K2, P2, N2 = map(int, input().split())
print(*fun(K1, M, K2, P2, N2))
# print(*fun2(K1, M, K2, P2, N2))

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # import random

    # for i in range(1000):
    #     s = [random.randint(1, 10) for _ in range(5)]
    #     if not fun(*s) == fun2(*s):
    #         print(f"{s}, \tTrue: {fun2(*s)}, \tMy: {fun(*s)}")
