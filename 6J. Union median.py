"""
Дано N упорядоченных по неубыванию последовательностей целых чисел (т.е. каждый
следующий элемент больше либо равен предыдущему), в каждой из последовательностей
ровно L элементов. Для каждых двух последовательностей выполняют следующую операцию:
объединяют их элементы (в объединенной последовательности каждое число будет идти
столько раз, сколько раз оно встречалось суммарно в объединяемых последовательностях),
упорядочивают их по неубыванию и смотрят, какой элемент в этой последовательности
из 2L элементов окажется на месте номер L (этот элемент называют левой медианой).
Напишите программу, которая для каждой пары последовательностей выведет левую медиану
их объединения.

Формат ввода
Сначала вводятся числа N и L (2 ≤ N ≤ 100, 1 ≤ L ≤ 300). В следующих N строках задаются
последовательности. Каждая последовательность состоит из L чисел, по модулю не превышающих
30000.

Формат вывода
В первой строке выведите медиану объединения 1-й и 2-й последовательностей, во второй
строке — объединения 1-й и 3-й, и так далее, в (N‑1)-ой строке — объединения 1-й
и N-ой последовательностей, далее медиану объединения 2-й и 3-й, 2-й и 4-й, и т.д.
до 2-й и N-ой, затем 3-й и 4-й и так далее. В последней строке должна быть выведена
медиана объединения (N–1)-й и N-ой последовательностей.

Пример
Ввод
Вывод
3 6
1 4 7 10 13 16
0 2 5 9 14 20
1 7 16 16 21 22

7
10
9
"""


def median_old(s1, s2):
    L = len(s1)
    return sorted(s1 + s2)[L - 1]


def median(a, b):
    L = len(a)

    a_index = b_index = 0
    while a_index + b_index < L - 1:  # (a + 1) + (b + 1) < L + 1
        if a[a_index] < b[b_index]:
            a_index += 1
        else:
            b_index += 1

    return min(a[a_index], b[b_index])


def fun(s):
    """
    >>> fun([[1, 4, 7, 10, 13, 16], [0, 2, 5, 9, 14, 20], [1, 7, 16, 16, 21, 22]])
    [7, 10, 9]
    """

    ans = []

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            ans.append(median(s[i], s[j]))

    return ans


N, L = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(N)]
print(*fun(s), sep="\n")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
