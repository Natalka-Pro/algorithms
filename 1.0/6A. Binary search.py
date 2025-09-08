"""
Реализуйте двоичный поиск в массиве

Формат ввода
В первой строке входных данных содержатся натуральные числа N и K (). Во второй
строке задаются N элементов первого массива, а в третьей строке – K элементов второго
массива. Элементы обоих массивов - целые числа, каждое из которых по модулю не превосходит
109

Формат вывода
Требуется для каждого из K чисел вывести в отдельную строку "YES", если это число
встречается в первом массиве, и "NO" в противном случае.

Пример 1
Ввод
Вывод
10 10
1 61 126 217 2876 6127 39162 98126 712687 1000000000
100 6127 1 61 200 -10000 1 217 10000 1000000000

NO
YES
YES
YES
NO
NO
YES
YES
NO
YES

Пример 2
Ввод
Вывод
10 10
-8 -6 -4 -4 -2 -1 0 2 3 3
8 3 -3 -2 2 -1 2 9 -8 0

NO
YES
NO
YES
YES
YES
YES
NO
YES
YES

Пример 3
Ввод
Вывод
10 5
1 2 3 4 5 6 7 8 9 10
-2 0 4 9 12

NO
NO
YES
YES
NO
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

    return mas[l] == x


def fun(mas, req):
    """
    >>> fun([1, 61, 126, 217, 2876, 6127, 39162, 98126, 712687, 1000000000], [100, 6127, 1, 61, 200, -10000, 1, 217, 10000, 1000000000])
    ['NO', 'YES', 'YES', 'YES', 'NO', 'NO', 'YES', 'YES', 'NO', 'YES']
    >>> fun([-8, -6, -4, -4, -2, -1, 0, 2, 3, 3], [8, 3, -3, -2, 2, -1, 2, 9, -8, 0])
    ['NO', 'YES', 'NO', 'YES', 'YES', 'YES', 'YES', 'NO', 'YES', 'YES']
    >>> fun([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [-2, 0, 4, 9, 12])
    ['NO', 'NO', 'YES', 'YES', 'NO']
    """

    ans = []
    for r in req:
        if lfind(mas, r):
            ans.append("YES")
        else:
            ans.append("NO")

    return ans


N, K = map(int, input().split())
mas = list(map(int, input().split()))
req = list(map(int, input().split()))
print(*fun(mas, req), sep="\n")

# print(f">>> fun({mas}, {req})")
# print(f"{fun(mas, req)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
