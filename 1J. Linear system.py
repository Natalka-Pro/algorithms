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
"""

# from math import isclose


def slau(a, b, c, d, e, f):
    det = a * d - b * c

    if det != 0:
        x0 = d * e - b * f
        y0 = -c * e + a * f
        x0 /= det
        y0 /= det
        return [2, x0, y0]
    elif b != 0 and d != 0:
        k = a / b
        if e / b == f / d:  # if isclose(e / b, f / d):
            if k != 0:
                return [1, -k, e / b]
            else:
                return [4, e / b]
        else:
            return [0]
    elif b == 0:
        if a == 0:
            if e != 0:
                return [0]
            else:  # a == b == e == 0 => cx + dy = f
                if d != 0:
                    k = -c / d
                    if k != 0:
                        return [1, k, f / d]
                    else:
                        return [4, f / d]
                else:  # d == 0 => cx = f
                    if c != 0:
                        return 3, f / c
                    elif f != 0:  # c == 0
                        return [0]
                    else:  # f == 0
                        return [5]
        else:  # a != 0 => d == 0
            if c != 0:
                if e / a == f / c:  # if isclose(e / a, f / c):
                    return [3, e / a]
                else:
                    return [0]
            elif f != 0:  # c == 0
                return [0]
            else:  # f == 0
                return [3, e / a]


l = []

for i in range(6):
    l.append(float(input()))


# print(*slau(*l))

a, b, c, d, e, f = l
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
print(*slau(*l))
# except TypeError: # ZeroDivisionError
# print(0)


# print(*slau(*l2))
# print(*slau(*l3))
# print(*slau(*l4))
