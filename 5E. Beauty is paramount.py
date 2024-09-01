"""
В парке города Питсбурга есть чудесная аллея, состоящая из N посаженных в один ряд
деревьев, каждое одного из K сортов. В связи с тем, что Питсбург принимает открытый
чемпионат Байтландии по программированию, было решено построить огромную арену для
проведения соревнований. Так, согласно этому плану вся аллея подлежала вырубке.
Однако министерство деревьев и кустов воспротивилось этому решению, и потребовало
оставить некоторые из деревьев в покое. Согласно новому плану строительства все
деревья, которые не будут вырублены, должны образовывать один непрерывный отрезок,
являющийся подотрезком исходного. Каждого из K видов деревьев требуется сохранить
хотя бы по одному экземпляру. На вас возложена задача найти отрезок наименьшей длины,
удовлетворяющий указанным ограничениям.

Формат ввода
В первой строке входного файла находятся два числа N и K (1 ≤ N, K ≤ 250000). Во
второй строке входного файла следуют N чисел (разделенных пробелами), i-ое число
второй строки задает цвет i-ого слева дерева в аллее. Гарантируется, что присутствует
хотя бы одно дерево каждого цвета

Формат вывода
В выходной файл выведите два числа, координаты левого и правого концов отрезка минимальной
длины, удовлетворяющего условию. Если оптимальных ответов несколько, выведите любой.

Пример 1
Ввод
Вывод
5 3
1 2 1 3 2

2 4

Пример 2
Ввод
Вывод
6 4
2 4 2 3 3 1

2 6
"""

from collections import Counter


class MultiSet(Counter):
    def add(self, key):
        if key not in self:
            self[key] = 0
        self[key] += 1

    def pop(self, key):
        if key in self:
            if self[key] == 1:
                super().pop(key)
            else:
                self[key] -= 1


def fun(s, K):
    """
    >>> fun([1, 2, 1, 3, 2], 3)
    (2, 4)
    >>> fun([2, 4, 2, 3, 3, 1], 4)
    (2, 6)
    """

    d = MultiSet()

    min_len = len(s) + 1
    ans = None

    right = 0

    for left in range(0, len(s)):
        d.pop(s[left - 1])

        while right < len(s) and len(d) != K:
            d.add(s[right])
            right += 1

        if len(d) == K and right - left < min_len:
            min_len = right - left
            ans = (left + 1, right)

    return ans


N, K = map(int, input().split())
s = list(map(int, input().split()))
print(*fun(s, K))
# print(f">>> fun({s}, {K})")
# print(f"{fun(s, K)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
