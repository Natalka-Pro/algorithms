"""
За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие
размером D × E. Замок Иф сложен из кирпичей, размером A × B × C. Определите, сможет
ли узник выбрасывать кирпичи в море через это отверстие, если стороны кирпича должны
быть параллельны сторонам отверстия.

Формат ввода
Программа получает на вход числа A, B, C, D, E.

Формат вывода
Программа должна вывести слово YES или NO.

Пример 1
Ввод
Вывод
1
1
1
1
1

YES

Пример 2
Ввод
Вывод
2
2
2
1
1

NO
"""


def fun(A, B, C, D, E):
    """
    >>> fun(1, 1, 1, 1, 1)
    'YES'
    >>> fun(2, 2, 2, 1, 1)
    'NO'
    >>> fun(1, 2, 3, 4, 5)
    'YES'
    >>> fun(1, 1, 3, 2, 2)
    'YES'
    """
    A, B, _ = sorted((A, B, C))  # ascending
    D, E = sorted((D, E))

    return "YES" if (A <= D) and (B <= E) else "NO"


A, B, C, D, E = [int(input()) for _ in range(5)]
print(fun(A, B, C, D, E))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
