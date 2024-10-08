"""
При реализации проекта «Умная школа» было решено в каждый учебный класс выбранной
для этого школы установить по кондиционеру нового поколения для автоматического
охлаждения и вентиляции воздуха. По проекту в каждом классе должен быть установлен
только один кондиционер и мощность кондиционера должна быть достаточной для размеров
класса. Чем больше класс, тем мощнее должен быть кондиционер.
Все классы школы пронумерованы последовательно от 1 до n. Известно, что для каждого
класса с номером i, требуется ровно один кондиционер, мощность которого больше или
равна ai ватт.
Администрации школы предоставили список из m различных моделей кондиционеров, которые
можно закупить. Для каждой модели кондиционера известна его мощность и стоимость.
Требуется написать программу, которая определит, за какую минимальную суммарную
стоимость кондиционеров можно оснастить все классы школы.

Формат ввода
Первая строка входного файла содержит одно целое число n (1 ≤ n ≤ 50 000) количество
классов в школе.
Вторая строка содержит n целых чисел ai (1 ≤ ai ≤ 1000) — минимальная мощность кондиционера
в ваттах, который можно установить в классе с номером i.
Третья строка содержит одно целое число m (1 ≤ m ≤ 50 000) — количество предложенных
моделей кондиционеров.
Далее, в каждой из m строк содержится пара целых чисел bj и cj (1 ≤ bj ≤ 1000, 1
≤ cj ≤ 1000) мощность в ваттах j-й модели кондиционера и его цена в рублях соответственно.

Формат вывода
Выходной файл должен содержать одно число минимальную суммарную стоимость кондиционеров
в рублях. Гарантируется, что хотя бы один корректный выбор кондиционеров существует,
и во всех классах можно установить подходящий кондиционер.

Пример 1
Ввод
Вывод
1
800
1
800 1000

1000

Пример 2
Ввод
Вывод
3
1 2 3
4
1 10
1 5
10 7
2 3

13

Примечания
В первом примере нужно купить один единственно возможный кондиционер за 1000 рублей.
Во втором примере оптимально будет установить в первом и втором классах кондиционеры
четвертого типа, а в третьем классе – кондиционер третьего типа. Суммарная стоимость
этих кондиционеров будет составлять 13 рублей (3 + 3 + 7).
"""


def fun(A, s):
    """
    # >>> fun([800], [(800, 1000)])
    # 1000
    >>> fun([1, 2, 3], [(1, 10), (1, 5), (10, 7), (2, 3)])
    13
    >>> fun([1, 2, 3], [(1, 10), (1, 5), (3, 3), (10, 7), (2, 3)])
    9
    """

    # s_power = sorted(s)
    price = sorted(s, key=lambda x: (x[1], -x[0]))

    price_new = [price[0]]

    for i in range(1, len(price)):
        if price[i][0] > price_new[-1][0]:
            price_new.append(price[i])

    def lfind(x, s):
        for i in range(len(s)):
            if s[i][0] >= x:
                return i

    def lfind_bin(x, s):
        l, r = 0, len(s) - 1
        while l < r:
            m = (l + r) // 2
            if s[m][0] >= x:
                r = m
            else:
                l = m + 1

        return l

    sum = 0
    for a in A:
        idx = lfind_bin(a, price_new)
        sum += price_new[idx][1]

    return sum


_ = int(input())
A = list(map(int, input().split()))
m = int(input())
s = [tuple(map(int, input().split())) for _ in range(m)]
print(fun(A, s))

# print(f">>> fun({A}, {s})")
# print(f"{fun(s)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
