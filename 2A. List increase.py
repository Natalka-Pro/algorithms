"""
Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли,
что каждый элемент этого списка больше предыдущего).
Выведите YES, если массив монотонно возрастает и NO в противном случае.

Пример 1
Ввод
Вывод
1 7 9

YES

Пример 2
Ввод
Вывод
1 9 7

NO

Пример 3
Ввод
Вывод
2 2 2

NO
"""


def fun(s):
    """
    >>> fun([1, 7, 9])
    'YES'
    >>> fun([1, 9, 7])
    'NO'
    >>> fun([2, 2, 2])
    'NO'
    """
    ans = True

    for i in range(len(s) - 1):
        if s[i] >= s[i + 1]:
            ans = False
            break

    return "YES" if ans else "NO"


s = list(map(int, input().split()))
print(fun(s))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
