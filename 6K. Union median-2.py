"""
Дано N упорядоченных по неубыванию последовательностей целых чисел (т.е. каждый
следующий элемент больше либо равен предыдущему), в каждой из последовательностей
ровно L элементов. Для каждых двух последовательностей выполняют следующую операцию:
объединяют их элементы (в объединенной последовательности каждое число будет идти
столько раз, сколько раз оно встречалось суммарно в объединяемых последовательностях),
упорядочивают их по неубыванию и смотрят, какой элемент в этой последовательности
из 2L элементов окажется на месте номер L (этот элемент называют левой медианой).
Напишите программу, которая для каждой пары последовательностей выведет левую медиану
их объединения.

Формат ввода
Сначала вводятся числа N и L (2 ≤ N ≤ 200, 1 ≤ L ≤ 50000). В следующих N строках
задаются параметры, определяющие последовательности.
Каждая последовательность определяется пятью целочисленными параметрами: x1, d1,
a, c, m. Элементы последовательности вычисляются по следующим формулам: x1 нам задано,
а для всех i от 2 до L: xi = xi–1+di–1. Последовательность di определяется следующим
образом: d1 нам задано, а для i ≥ 2 di = ((a*di–1+c) mod m), где mod – операция
получения остатка от деления (a*di–1+c) на m.
Для всех последовательностей выполнены следующие ограничения: 1 ≤ m ≤ 40000, 0 ≤
a < m, 0≤c<m, 0≤d1<m. Гарантируется, что все члены всех последовательностей по модулю
не превышают 109.

Формат вывода
В первой строке выведите медиану объединения 1-й и 2-й последовательностей, во второй
строке — объединения 1-й и 3-й, и так далее, в (N‑1)-ой строке — объединения 1-й
и N-ой последовательностей, далее медиану объединения 2-й и 3-й, 2-й и 4-й, и т.д.
до 2-й и N-ой, затем 3-й и 4-й и так далее. В последней строке должна быть выведена
медиана объединения (N–1)-й и N-ой последовательностей.

Пример
Ввод
Вывод
3 6
1 3 1 0 5
0 2 1 1 100
1 6 8 5 11

7
10
9

Примечания
Последовательности, объединения которых мы считаем, таковы:
1 4 7 10 13 16
0 2 5 9 14 20
1 7 16 16 21 22
"""

from functools import partial


def seq_full(x, d, a, c, m, L):
    seq = [None] * L
    seq[0] = x
    i = 1
    while i < L:
        x = x + d
        seq[i] = x
        d = (a * d + c) % m
        i += 1

    return seq


def lfind(l, r, check):
    while l < r:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m + 1

    return l


def rfind(l, r, check):
    while l < r:
        m = (l + r + 1) // 2
        if check(m):
            l = m
        else:
            r = m - 1

    return l


def num_greater_x(s, x):
    if x >= s[-1]:
        return 0

    return len(s) - lfind(0, len(s) - 1, lambda m: s[m] > x)


def num_lower_x(s, x):
    if x <= s[0]:
        return 0

    return 1 + rfind(0, len(s) - 1, lambda m: s[m] < x)


def check(m, a, b, L):
    num_g = num_greater_x(a, m) + num_greater_x(b, m)
    num_l = num_lower_x(a, m) + num_lower_x(b, m)

    if num_l <= L - 1 and num_g <= L:
        return 0
    elif num_l >= L:
        return -1
    elif num_g > L:
        return 1


def mid_find(l, r, check):
    while l < r:
        m = (l + r) // 2
        res = check(m)

        # print(f"{m=}, {l=}, {r=}, {res=}")

        if res == -1:
            r = m - 1
        elif res == 1:
            l = m + 1
        elif res == 0:
            return m

    return l


def median_bin(s1, s2, L):
    a, b = seq_full(*s1, L), seq_full(*s2, L)
    # a, b = s1, s2

    f = partial(check, a=a, b=b, L=L)
    return mid_find(min(a[0], b[0]), max(a[-1], b[-1]), f)


def fun(s, L):
    """
    >>> fun([[1, 3, 1, 0, 5], [0, 2, 1, 1, 100], [1, 6, 8, 5, 11]], 6)
    [7, 10, 9]
    """

    ans = []

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            ans.append(median_bin(s[i], s[j], L))

    return ans


def seq(x, d, a, c, m, L):
    yield x
    i = 0
    while i < L - 1:
        x = x + d
        yield x
        d = (a * d + c) % m
        i += 1


def median(s1, s2, L):

    a, b = seq(*s1, L), seq(*s2, L)
    a_val, b_val = next(a), next(b)
    a_index = b_index = 0

    while a_index + b_index < L - 1:  # (a + 1) + (b + 1) < L + 1

        if a_val < b_val:
            a_index += 1
            a_val = next(a)
        else:
            b_index += 1
            b_val = next(b)

    return min(a_val, b_val)


def fun2(s, L):
    """
    TL - 14 test

    >>> fun2([[1, 3, 1, 0, 5], [0, 2, 1, 1, 100], [1, 6, 8, 5, 11]], 6)
    [7, 10, 9]
    """

    ans = []

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            ans.append(median(s[i], s[j], L))

    return ans


N, L = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(N)]
print(*fun(s, L), sep="\n")

# print(f">>> fun({s}, {L})")
# print(f"    {fun(s, L)}")


# if __name__ == "__main__":
#     import doctest

#     doctest.testmod()

#     import random

#     for i in range(1000):
#         # N = random.randint(2, 200)
#         # L = random.randint(1, 50000)

#         # N = random.randint(2, 100)
#         N = 2
#         L = random.randint(1, 50000)

#         s = [None] * N
#         for i in range(N):
#             # m = random.randint(1, 40000)
#             # a = c = d = random.randint(0, m)
#             m = random.randint(1, 40000)
#             a = c = d = random.randint(0, 0)
#             x = random.randint(-10**9, 10**9)

#             s[i] = [x, d, a, c, m]

#         # print(N, L)
#         # ans1 = fun(s, L)
#         # print("fun")
#         # ans2 = fun2(s, L)
#         # print("fun2")

#         ans1 = median_bin(s[0], s[1], L)
#         ans2 = median(s[0], s[1], L)

#         # print(ans1, ans2)

#         if not (ans1 == ans2):
#             print(f"{s, L}, \tTrue: {ans2}, \tMy: {ans1}")
