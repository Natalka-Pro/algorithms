"""
Даны числа a, b, c, d, e, f. Решите систему линейных уравнений
ax + by = e
cx + dy = f

Формат ввода
Вводятся 6 вещественных чисел - коэффициенты уравнений.

Формат вывода
Вывод программы зависит от вида решения этой системы. Если система не имеет решений,
то программа должна вывести единственное число 0. Если система имеет бесконечно
много решений, каждое из которых имеет вид y=kx+b, то программа должна вывести число
1, а затем значения k и b. Если система имеет единственное решение (x0,y0), то программа
должна вывести число 2, а затем значения x0 и y0. Если система имеет бесконечно
много решений вида x=x0, y — любое, то программа должна вывести число 3, а затем
значение x0. Если система имеет бесконечно много решений вида y=y0, x — любое, то
программа должна вывести число 4, а затем значение y0. Если любая пара чисел (x,y)
является решением, то программа должна вывести число 5.
Числа x0 и y0 будут проверяться с точностью до пяти знаков после точки.

Пример 1
Ввод
Вывод
1
0
0
1
3
3

2 3 3

Пример 2
Ввод
Вывод
1
1
2
2
1
2

1 -1 1

Пример 3
Ввод
Вывод
0
2
0
4
1
2

4 0.5

https://python.su/forum/topic/33279/
"""

# import random
# from math import isclose


def fun(a, b, c, d, e, f):
    """
    >>> fun(1, 0, 0, 1, 3, 3)
    (2, 3.0, 3.0)
    >>> fun(1, 1, 2, 2, 1, 2)
    (1, -1.0, 1.0)
    >>> fun(0, 2, 0, 4, 1, 2)
    (4, 0.5)
    """

    det = a * d - b * c
    delta_x = d * e - b * f
    delta_y = -c * e + a * f

    if det != 0:
        return 2, delta_x / det, delta_y / det
    elif b != 0 and d != 0:
        k = a / b
        if delta_x == 0:  # e / b == f / d:
            if k != 0:
                return 1, -k, e / b
            else:
                return 4, e / b
        else:
            return (0,)
    elif b == 0:
        if a == 0:
            if e != 0:
                return (0,)
            else:  # a == b == e == 0 => cx + dy = f
                if d != 0:
                    k = -c / d
                    if k != 0:
                        return 1, k, f / d
                    else:
                        return 4, f / d
                else:  # d == 0 => cx = f
                    if c != 0:
                        return 3, f / c
                    elif f != 0:  # c == 0
                        return (0,)
                    else:  # f == 0
                        return (5,)
        else:  # a != 0 => d == 0
            if c != 0:
                if e / a == f / c:  # if isclose(e / a, f / c):
                    return 3, e / a
                else:
                    return (0,)
            elif f != 0:  # c == 0
                return (0,)
            else:  # f == 0
                return 3, e / a


def fun2(a, b, c, d, e, f):
    delta = a * d - b * c
    delta_x = e * d - b * f
    delta_y = a * f - c * e
    if delta == 0:
        if a == b == c == d == e == f == 0:
            return [5]
        elif a == b == 0 and e != 0:
            return [0]
        elif c == d == 0 and f != 0:
            return [0]
        elif delta_x == 0:
            if a == c == 0:
                return 4, f / d if b == 0 else e / b
            elif b == d == 0:
                return (3, f / c if a == 0 else e / a) if delta_y == 0 else [0]
            else:
                return (1, -a / b, e / b) if d == 0 else (1, -c / d, f / d)
        else:
            return [0]
    else:
        return 2, delta_x / delta, delta_y / delta


l = [float(input()) for _ in range(6)]
print(*fun(*l))


# for i in range(10):
#     l = [float(random.randint(-100, 100)) for _ in range(6)]

#     res1, res2 = fun(*l), fun2(*l)

#     print(l, res1)

#     if len(res1) != len(res2):
#         print(l, "не равна длина")

#     eq = [isclose(res1[i], res2[i]) for i in range(len(res1))]

#     # print(eq)

#     if not all(eq):
#         print(res1, res2)


# a, b, c, d, e, f = l
# l2 = c, d, a, b, f, e
# l3 = b, a, d, c, e, f
# l4 = d, c, b, a, f, e

# s = "{0}x + {1}y = {4}\n{2}x + {3}y = {5}".format(*l)
# print(s)
# s = "{0}x + {1}y = {4}\n{2}x + {3}y = {5}".format(*l2)
# print(s)
# s = "{0}x + {1}y = {4}\n{2}x + {3}y = {5}".format(*l3)
# print(s)
# s = "{0}x + {1}y = {4}\n{2}x + {3}y = {5}".format(*l4)
# print(s)

# try:
# print(*slau(*l))
# except TypeError: # ZeroDivisionError
# print(0)


# print(*slau(*l2))
# print(*slau(*l3))
# print(*slau(*l4))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
