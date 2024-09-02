"""
Сегодня утром жюри решило добавить в вариант олимпиады еще одну, Очень Легкую Задачу.
Ответственный секретарь Оргкомитета напечатал ее условие в одном экземпляре, и теперь
ему нужно до начала олимпиады успеть сделать еще N копий. В его распоряжении имеются
два ксерокса, один из которых копирует лист за х секунд, а другой – за y. (Разрешается
использовать как один ксерокс, так и оба одновременно. Можно копировать не только
с оригинала, но и с копии.) Помогите ему выяснить, какое минимальное время для этого
потребуется.

Формат ввода
На вход программы поступают три натуральных числа N, x и y, разделенные пробелом
(1 ≤ N ≤ 2 × 108, 1 ≤ x, y ≤ 10).

Формат вывода
Выведите одно число – минимальное время в секундах, необходимое для получения N
копий.

Пример 1
Ввод
Вывод
4 1 1

3

Пример 2
Ввод
Вывод
5 1 2

4
"""


def check(time, params):
    N, x, y = params

    max_x = time // x
    max_y = time // y

    return max_x + max_y >= N


def lfind(l, r, params):
    while l < r:
        m = (l + r) // 2
        if check(m, params):
            r = m
        else:
            l = m + 1

    return l


def fun(N, x, y):
    """
    >>> fun(4, 1, 1)
    3
    >>> fun(5, 1, 2)
    4
    """

    x, y = sorted([x, y])
    # первую копию делаем за x секунд
    return x + lfind(0, x * (N - 1), (N - 1, x, y))


N, x, y = map(int, input().split())
print(fun(N, x, y))

# print(f">>> fun({N}, {x}, {y})")
# print(f"    {fun(N, x, y)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
