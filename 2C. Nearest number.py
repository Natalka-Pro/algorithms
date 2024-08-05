"""
Напишите программу, которая находит в массиве элемент, самый близкий по величине
к  данному числу.

Формат ввода
В первой строке задается одно натуральное число N, не превосходящее 1000 – размер
массива. Во второй строке содержатся N чисел – элементы массива (целые числа, не
превосходящие по модулю 1000). В третьей строке вводится одно целое число x, не
превосходящее по модулю 1000.

Формат вывода
Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько, выведите
любое из них.

Пример 1
Ввод
Вывод
5
1 2 3 4 5
6

5

Пример 2
Ввод
Вывод
5
5 4 3 2 1
3

3
"""


def dist(a, b):
    return abs(a - b)


def fun(s, x):
    """
    >>> fun([1, 2, 3, 4, 5], 6)
    5
    >>> fun([5, 4, 3, 2, 1], 3)
    3
    """
    ans = s[0]

    for elem in s:
        if dist(elem, x) < dist(ans, x):
            ans = elem

    return ans


_, s, x = int(input()), list(map(int, input().split())), int(input())
print(fun(s, x))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
