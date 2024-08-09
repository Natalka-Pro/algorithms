"""
В данном списке из n ≤ 10^5 целых чисел найдите три числа,
произведение которых максимально.
Решение должно иметь сложность O(n), где n - размер списка.
Выведите три искомых числа в любом порядке.

Пример 1
Ввод
Вывод
3 5 1 7 9 0 9 -3 10

10 9 9

Пример 2
Ввод
Вывод
-5 -30000 -12

-5 -12 -30000

Пример 3
Ввод
Вывод
1 2 3

3 2 1
"""


def update(top, elem, max_len, reverse=False):
    top.append(elem)
    top = sorted(top, reverse=reverse)
    if len(top) == max_len + 1:
        top = top[:max_len]

    return top


def fun(s):
    """
    >>> fun([3, 5, 1, 7, 9, 0, 9, -3, -2, 10])
    (10, 9, 9)
    >>> fun([-5, -30000, -12, 1, 2])
    (2, -12, -30000)
    >>> fun([1, 2, 3])
    (3, 2, 1)
    >>> fun([1, 2, 3, 4, 5, -5, -6, -7])
    (5, -6, -7)
    >>> fun([1, 2, 3, 4, 5, -5, -2, -3])
    (5, -3, -5)
    >>> fun([-1, -2, -3, -4])
    (-1, -2, -3)
    """
    maxs_3 = []
    mins_2 = []

    for i in s:
        maxs_3 = update(maxs_3, i, max_len=3, reverse=True)
        mins_2 = update(mins_2, i, max_len=2)

    ans1, ans2 = maxs_3, (maxs_3[0], *mins_2)
    ans = max(ans1, ans2, key=lambda x: x[0] * x[1] * x[2])

    return tuple(sorted(ans, reverse=True))


def fun2(s):
    """
    >>> fun2([3, 5, 1, 7, 9, 0, 9, -3, -2, 10])
    (10, 9, 9)
    >>> fun2([-5, -30000, -12, 1, 2])
    (2, -12, -30000)
    >>> fun2([1, 2, 3])
    (3, 2, 1)
    >>> fun2([1, 2, 3, 4, 5, -5, -6, -7])
    (5, -6, -7)
    >>> fun2([1, 2, 3, 4, 5, -5, -2, -3])
    (5, -3, -5)
    >>> fun2([-1, -2, -3, -4])
    (-1, -2, -3)
    """

    s = sorted(s, reverse=True)

    ans1, ans2 = s[:3], (s[0], *s[-2:])
    ans = max(ans1, ans2, key=lambda x: x[0] * x[1] * x[2])

    return tuple(sorted(ans, reverse=True))


s = list(map(int, input().split()))
print(*fun(s))
# print(*fun2(s))

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # import numpy as np

    # for i in range(1000):
    #     s = list(np.random.randint(-100, 101, 10))
    #     if not fun(s) == fun2(s):
    #         print(s)
