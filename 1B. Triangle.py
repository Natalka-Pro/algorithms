"""
Даны три натуральных числа. Возможно ли построить треугольник с такими сторонами.
Если это возможно, выведите строку YES, иначе выведите строку NO.
Треугольник — это три точки, не лежащие на одной прямой.

Формат ввода
Вводятся три натуральных числа.

Формат вывода
Выведите ответ на задачу.

Пример 1
Ввод
Вывод
3
4
5

YES

Пример 2
Ввод
Вывод
3
5
4

YES

Пример 3
Ввод
Вывод
4
5
3

YES
"""


def fun(*l):
    """
    >>> fun(3, 4, 5)
    'YES'
    >>> fun(3, 5, 4)
    'YES'
    >>> fun(4, 5, 3)
    'YES'
    """
    for i in range(3):
        if l[i] >= sum(l[:i]) + sum(l[i + 1 :]):
            return "NO"
    else:
        return "YES"


a, b, c = [int(input()) for _ in range(3)]
print(fun(a, b, c))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
