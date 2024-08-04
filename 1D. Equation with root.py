"""
Решите в целых числах уравнение:
sqrt(ax + b) = c,
a, b, c – данные целые числа: найдите все решения или сообщите, что решений в целых
числах нет.

Формат ввода
Вводятся три числа a, b и c по одному в строке.

Формат вывода
Программа должна вывести все решения уравнения в порядке возрастания, либо NO SOLUTION
(заглавными буквами), если решений нет. Если решений бесконечно много, вывести MANY
SOLUTIONS.

Пример 1
Ввод
Вывод
1
0
0

0

Пример 2
Ввод
Вывод
1
2
3

7

Пример 3
Ввод
Вывод
1
2
-3

NO SOLUTION
"""


def fun(a, b, c):
    """
    >>> fun(1, 0, 0)
    0
    >>> fun(1, 2, 3)
    7
    >>> fun(1, 2, -3)
    'NO SOLUTION'
    """
    if c < 0:
        return "NO SOLUTION"
    elif c == 0:  # ax + b = 0
        if a == 0:
            if b != 0:
                return "NO SOLUTION"
            else:
                return "MANY SOLUTIONS"
        else:
            ans = -b / a
            if int(ans) == ans:
                return int(ans)
            else:
                return "NO SOLUTION"
    else:  # ax + b = c^2
        if a == 0:
            if b != c**2:
                return "NO SOLUTION"
            else:
                return "MANY SOLUTIONS"
        else:
            ans = (c**2 - b) / a
            if int(ans) == ans:
                return int(ans)
            else:
                return "NO SOLUTION"


a, b, c = int(input()), int(input()), int(input())
print(fun(a, b, c))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
