"""
Последовательность чисел назовем симметричной, если она одинаково читается как слева
направо, так и справа налево. Например, следующие последовательности являются симметричными:
1 2 3 4 5 4 3 2 1
1 2 1 2 2 1 2 1
Вашей программе будет дана последовательность чисел. Требуется определить, какое
минимальное количество и каких чисел надо приписать в конец этой последовательности,
чтобы она стала симметричной.

Формат ввода
Сначала вводится число N — количество элементов исходной последовательности (1 ≤
N ≤ 100). Далее идут N чисел — элементы этой последовательности, натуральные числа
от 1 до 9.

Формат вывода
Выведите сначала число M — минимальное количество элементов, которое надо дописать
к последовательности, а потом M чисел (каждое — от 1 до 9) — числа, которые надо
дописать к последовательности.

Пример 1
Ввод
Вывод
9
1 2 3 4 5 4 3 2 1

0

Пример 2
Ввод
Вывод
5
1 2 1 2 2

3
1 2 1

Пример 3
Ввод
Вывод
5
1 2 3 4 5

4
4 3 2 1
"""


def fun(s):
    """
    >>> fun([1, 2, 3, 4, 5, 4, 3, 2, 1])
    0
    >>> fun([1, 2, 1, 2, 2])
    (3, [1, 2, 1])
    >>> fun([1, 2, 3, 4, 5])
    (4, [4, 3, 2, 1])
    """

    new_s = s
    k = 0

    while True:
        if new_s == new_s[::-1]:
            break
        else:
            k += 1
            new_s = s + s[k - 1 :: -1]  # s[:k][::-1]

    if k == 0:
        return k
    else:
        return k, s[k - 1 :: -1]  # s[:k][::-1]


_, s = int(input()), list(map(int, input().split()))
ans = fun(s)
if type(ans) is int:
    print(ans)
else:
    print(ans[0])
    print(*ans[1])

if __name__ == "__main__":
    import doctest

    doctest.testmod()