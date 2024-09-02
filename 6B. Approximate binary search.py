"""
Для каждого из чисел второй последовательности найдите ближайшее к нему в первой.

Формат ввода
В первой строке входных данных содержатся числа N и K (). Во второй строке задаются
N чисел первого массива, отсортированного по неубыванию, а в третьей строке – K
чисел второго массива. Каждое число в обоих массивах по модулю не превосходит 2⋅109.

Формат вывода
Для каждого из K чисел выведите в отдельную строку число из первого массива, наиболее
близкое к данному. Если таких несколько, выведите меньшее из них.

Пример 1
Ввод
Вывод
5 5
1 3 5 7 9
2 4 8 1 6

1
3
7
1
5

Пример 2
Ввод
Вывод
6 11
1 1 4 4 8 120
1 2 3 4 5 6 7 8 63 64 65

1
1
4
4
4
4
8
8
8
8
120

Пример 3
Ввод
Вывод
10 10
-5 1 1 3 5 5 8 12 13 16
0 3 7 -17 23 11 0 11 15 7

1
3
8
-5
16
12
1
12
16
8
"""


def check(mas, m, x):
    return mas[m] >= x


def lfind(mas, x):
    l, r = 0, len(mas) - 1
    while l < r:
        m = (l + r) // 2
        if check(mas, m, x):
            r = m
        else:
            l = m + 1

    return l


def nearest(x, mas):
    min_dist = abs(x - mas[0]) + 1
    min_elem = None

    for m in mas:
        dist = abs(m - x)

        if dist < min_dist:
            min_dist = dist
            min_elem = m

    return min_elem


def fun(mas, req):
    """
    >>> fun([1, 3, 5, 7, 9], [2, 4, 8, 1, 6])
    [1, 3, 7, 1, 5]
    >>> fun([1, 1, 4, 4, 8, 120], [1, 2, 3, 4, 5, 6, 7, 8, 63, 64, 65])
    [1, 1, 4, 4, 4, 4, 8, 8, 8, 8, 120]
    >>> fun([-5, 1, 1, 3, 5, 5, 8, 12, 13, 16], [0, 3, 7, -17, 23, 11, 0, 11, 15, 7])
    [1, 3, 8, -5, 16, 12, 1, 12, 16, 8]
    """

    ans = []
    for r in req:
        idx = lfind(mas, r)

        if idx == 0:
            ans.append(mas[idx])
        else:
            pos = idx - 1
            ans.append(nearest(r, [mas[pos], mas[idx]]))

    return ans


N, K = map(int, input().split())
mas = list(map(int, input().split()))
req = list(map(int, input().split()))
print(*fun(mas, req), sep="\n")

# print(f">>> fun({mas}, {req})")
# print(f"    {fun(mas, req)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
