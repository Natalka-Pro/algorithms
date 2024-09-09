"""
Дано n отрезков на числовой прямой и m точек на этой же прямой. Для каждой из данных
точек определите, скольким отрезкам они принадлежат. Точка x считается принадлежащей
отрезку с концами a и b, если выполняется двойное неравенство min(a, b) ≤ x ≤ max(a,
b).

Формат ввода
Первая строка содержит два целых числа n (1 ≤ n ≤ 105) – число отрезков и m (1 ≤
m ≤ 105) – число точек. В следующих n строках по два целых числи ai и bi – координаты
концов соответствующего отрезка. В последней строке m целых чисел – координаты точек.
Все числа по модулю не превосходят 109

Формат вывода
В выходной файл выведите m чисел – для каждой точки количество отрезков, в которых
она содержится.

Пример
Ввод
Вывод
3 2
0 5
-3 2
7 10
1 6

2 0
"""

IN = -1
CHECK = 0
OUT = 1


def fun(segments, points):
    """
    >>> fun([(0, 5), (-3, 2), (7, 10)], [1, 6])
    [2, 0]
    >>> fun([(0, 5), (-3, 2), (7, 10)], [6, 1])
    [0, 2]
    """

    N, M = len(segments), len(points)

    events = [None] * (N * 2 + M)

    for i, (start, end) in enumerate(segments):
        start, end = sorted([start, end])
        events[2 * i] = (start, IN)
        events[2 * i + 1] = (end, OUT)

    for i, point in enumerate(points):
        events[2 * N + i] = (point, CHECK)

    events.sort()

    num = 0  # число наблюдателей
    ans = {p: 0 for p in points}  # чтобы вывести в порядке points!!!

    for event in events:
        point, type = event
        if type == IN:
            num += 1
        elif type == CHECK:
            ans[point] = num
        elif type == OUT:
            num -= 1

    return [ans[p] for p in points]


N, M = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(N)]
points = list(map(int, input().split()))
print(*fun(segments, points))

# print(f">>> fun({segments}, {points})")
# print(f"    {fun(segments, points)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
