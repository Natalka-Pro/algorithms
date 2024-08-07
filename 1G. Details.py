"""
Имеется N кг металлического сплава. Из него изготавливают заготовки массой K кг
каждая. После этого из каждой заготовки вытачиваются детали массой M кг каждая (из
каждой заготовки вытачивают максимально возможное количество деталей). Если от заготовок
после этого что-то остается, то этот материал возвращают к началу производственного
цикла и сплавляют с тем, что осталось при изготовлении заготовок. Если того сплава,
который получился, достаточно для изготовления хотя бы одной заготовки, то из него
снова изготавливают заготовки, из них – детали и т.д. Напишите программу, которая
вычислит, какое количество деталей может быть получено по этой технологии из имеющихся
исходно N кг сплава.

Формат ввода
Вводятся N, K, M. Все числа натуральные и не превосходят 200.

Формат вывода
Выведите одно число — количество деталей, которое может получиться по такой технологии.

Пример 1
Ввод
Вывод
10 5 2

4

Пример 2
Ввод
Вывод
13 5 3

3

Пример 3
Ввод
Вывод
14 5 3

4
"""


def fun(N, K, M):
    """
    >>> fun(10, 5, 2)
    4
    >>> fun(13, 5, 3)
    3
    >>> fun(14, 5, 3)
    4
    """
    det = 0
    ost = N
    while ost >= K:
        col_zag, ost1 = ost // K, ost % K
        if K < M:
            break
        col_det, ost2 = K // M, K % M
        col_det *= col_zag
        ost2 *= col_zag
        det += col_det
        ost = ost1 + ost2

    return det


N, K, M = map(int, input().split())
print(fun(N, K, M))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
