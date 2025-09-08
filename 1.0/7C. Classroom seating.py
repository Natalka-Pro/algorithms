"""
Экзамен по берляндскому языку проходит в узкой и длинной аудитории. На экзамен пришло
N студентов. Все они посажены в ряд. Таким образом, позиция каждого человека задается
координатой на оси Ox (эта ось ведет вдоль длинной аудитории). Два человека могут
разговаривать, если расстояние между ними меньше или равно D. Какое наименьшее количество
типов билетов должен подготовить преподаватель, чтобы никакие два студента с одинаковыми
билетами не могли разговаривать? Выведите способ раздачи преподавателем билетов.

Формат ввода
В первой строке входного файла содержится два целых числа N, D (1 ≤ N ≤ 10000; 0 ≤ D ≤ 106).
Вторая строка содержит последовательность различных целых чисел X1, X2, ..., XN,
где Xi (0 ≤ Xi ≤ 106) обозначает координату вдоль оси Ox i-го студента

Формат вывода
В первую строчку выходного файла выведите количество вариантов, а во вторую, разделяя
пробелами, номера вариантов студентов в том порядке, в каком они перечислены во
входном файле.

Пример 1
Ввод
Вывод
4 1
11 1 12 2

2
1 1 2 2

Пример 2
Ввод
Вывод
4 0
11 1 12 2

1
1 1 1 1
"""

IN = -1
OUT = 1


def find_false(l):
    i = 0
    while i < len(l) and l[i]:
        i += 1

    return i


def fun(points, D):
    """
    >>> fun([11, 1, 12, 2], 1)
    (2, [1, 1, 2, 2])
    >>> fun([11, 1, 12, 2], 0)
    (1, [1, 1, 1, 1])
    """

    N = len(points)
    events = [None] * 2 * N

    if D == 0:
        return 1, [1 for _ in range(N)]

    for i, point in enumerate(points):
        start = max(point - D, 0)
        events[2 * i] = (start, IN, point)

        # end = min(point + D, N) !!!
        events[2 * i + 1] = (point, OUT, point)

    events.sort()

    max_var = 0
    cur_var = 0  # счётчик текущего числа студентов
    variants = []
    ans = {p: 0 for p in points}

    for e in events:
        _, type, point = e

        if type == IN:
            cur_var += 1

            if cur_var > max_var:
                variants.append(False)
                max_var = cur_var
                var = len(variants) - 1
            else:
                var = find_false(variants)

            ans[point] = var
            variants[var] = True

        elif type == OUT:
            cur_var -= 1
            var = ans[point]
            variants[var] = False

    return max_var, [ans[p] + 1 for p in points]


N, D = map(int, input().split())
points = list(map(int, input().split()))
max_var, ans = fun(points, D)
print(max_var)
print(*ans)

# print(f">>> fun({points}, {D})")
# print(f"    {fun(points, D)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
