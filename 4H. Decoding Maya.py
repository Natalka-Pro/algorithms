"""
Расшифровка письменности Майя оказалась более сложной задачей, чем предполагалось
ранними исследованиями. На протяжении более чем двух сотен лет удалось узнать не
так уж много. Основные результаты были получены за последние 30 лет.
Письменность Майя основывается на маленьких рисунках, известных как значки, которые
обозначают звуки. Слова языка Майя обычно записываются с помощью этих значков, которые
располагаются рядом друг с другом в некотором порядке.
Одна из проблем расшифровки письменности Майя заключается в определении этого порядка.
Рисуя значки некоторого слова, писатели Майя иногда выбирали позиции для значков,
исходя скорее из эстетических взглядов, а не определенных правил. Это привело к
тому, что, хотя звуки для многих значков известны, археологи не всегда уверены,
как должно произноситься записанное слово.
Археологи ищут некоторое слово W. Они знают значки для него, но не знают все возможные
способы их расположения. Поскольку они знают, что Вы приедете на IOI ’06, они просят
Вас о помощи. Они дадут Вам g значков, составляющих слово W, и последовательность
S всех значков в надписи, которую они изучают, в порядке их появления. Помогите
им, подсчитав количество возможных появлений слова W.
Задание Напишите программу, которая по значкам слова W и по последовательности S
значков надписи подсчитывает количество всех возможных вхождений слова W в S, то
есть количество всех различных позиций идущих подряд g значков в последовательности
S, которые являются какой-либо перестановкой значков слова W .

Формат ввода
1 ≤ g ≤ 3 000, g – количество значков в слове W
g ≤ |S| ≤ 3 000 000 где |S| – количество значков в последовательности S
На вход программы поступают данные в следующем формате:
СТРОКА 1: Содержит два числа, разделенных пробелом – g и |S|. СТРОКА 2: Содержит
g последовательных символов, с помощью которых записывается слово W . Допустимы
символы: ‘a’-‘z’ и ‘A’-‘Z’; большие и маленькие буквы считаются различными. СТРОКА
3: Содержит |S| последовательных символов, которые представляют значки в надписи.
Допустимы символы: ‘a’-‘z’ и ‘A’-‘Z’; большие и маленькие буквы считаются различными.

Формат вывода
Единственная строка выходных данных программы должна содержать количество возможных
вхождений слова W в S.

Пример
Ввод
Вывод
4 11
cAda
AbrAcadAbRa

2
"""

from collections import Counter
from itertools import chain


class MultiSet_old:
    def __init__(self):
        self.d = {}

    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            return 0

    def __contains__(self, key):
        return key in self.d

    def __len__(self):
        return len(self.d)

    def __str__(self):
        return self.d.__str__()

    def add(self, key):
        if key not in self.d:
            self.d[key] = 0
        self.d[key] += 1

    def pop(self, key):
        if key in self.d:
            if self.d[key] == 1:
                self.d.pop(key)
            else:
                self.d[key] -= 1


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


def non_equal(d1, d2):
    non_equal_num = 0

    for i in chain(range(ord("A"), ord("Z") + 1), range(ord("a"), ord("z") + 1)):

        letter = chr(i)

        if ((letter in d1) + (letter in d2)) % 2 == 1:
            non_equal_num += 1
        elif letter in d1:
            if d1[letter] != d2[letter]:
                non_equal_num += 1

    return non_equal_num


def fun(w, s):
    """
    >>> fun("cAda", "AbrAcadAbRa")
    2
    >>> fun("cAda", "qweqqweqweAbrAcadAbRacAda")
    4
    >>> fun("xrvv", "vrvx")
    1
    """

    dict_w = Counter(w)
    ans = 0
    cur_w = MultiSet()

    for i in s[: len(w)]:
        cur_w.add(i)

    non_equal_num = non_equal(dict_w, cur_w)
    if non_equal_num == 0:
        ans += 1

    # print(non_equal_num)

    for i in range(len(w), len(s)):
        old = s[i - len(w)]

        old_num = cur_w[old]
        true_num = dict_w[old]

        cur_w.pop(old)

        if old_num == true_num:
            non_equal_num += 1
        elif old_num - 1 == true_num:
            non_equal_num -= 1

        # print(old, cur_w[old], dict_w[old], non_equal_num)

        cur = s[i]

        old_num = cur_w[cur]
        true_num = dict_w[cur]

        cur_w.add(cur)

        if old_num == true_num:
            non_equal_num += 1
        elif old_num + 1 == true_num:
            non_equal_num -= 1

        # print(cur, cur_w[cur], dict_w[cur], non_equal_num)

        if non_equal_num == 0:
            ans += 1

    return ans


def equal(d1, d2):
    for i in chain(range(ord("A"), ord("Z") + 1), range(ord("a"), ord("z") + 1)):

        letter = chr(i)

        if ((letter in d1) + (letter in d2)) % 2 == 1:
            return False

        if letter in d1:
            if d1[letter] != d2[letter]:
                return False

    return True


def fun1(w, s):
    """
    TL - 13 test

    >>> fun1("cAda", "AbrAcadAbRa")
    2
    >>> fun1("cAda", "qweqqweqweAbrAcadAbRacAda")
    4
    >>> fun1("xrvv", "vrvx")
    1
    """

    dict_w = Counter(w)
    ans = 0
    cur_w = MultiSet()

    for i in s[: len(w)]:
        cur_w.add(i)

    if equal(dict_w, cur_w):
        ans += 1

    for i in range(len(w), len(s)):
        cur_w.pop(s[i - len(w)])
        cur_w.add(s[i])

        if equal(dict_w, cur_w):
            ans += 1

    return ans


def update(d, elem):
    if elem not in d:
        d[elem] = 0
    d[elem] += 1


def fun2(w, s):
    """
    TL - 13 test

    >>> fun2("cAda", "AbrAcadAbRa")
    2
    >>> fun2("cAda", "qweqqweqweAbrAcadAbRacAda")
    4
    >>> fun2("xrvv", "vrvx")
    1
    """

    dict_w = Counter(w)
    ans = 0
    prev_ok = False

    for i in range(len(s) - len(w) + 1):

        if s[i] in dict_w:

            if prev_ok and s[i - 1] == s[i + len(w) - 1]:
                ans += 1
                continue
            else:

                cur_w = {s[i]: 1}
                for k in range(i + 1, i + len(w)):
                    if s[k] in dict_w:
                        update(cur_w, s[k])

                        if cur_w[s[k]] > dict_w[s[k]]:
                            prev_ok = False
                            break
                    else:
                        prev_ok = False
                        break
                else:
                    ans += 1
                    prev_ok = True

    return ans


def fun3(w, s):
    """
    TL - 13 test

    >>> fun3("cAda", "AbrAcadAbRa")
    2
    >>> fun3("cAda", "qweqqweqweAbrAcadAbRacAda")
    4
    """

    w_set = set(w)
    w = sorted(w)

    ans = 0

    for i in range(len(s) - len(w) + 1):
        if s[i] in w_set and sorted(s[i : i + len(w)]) == w:
            ans += 1

    return ans


# for i in range(ord("A"), ord("z") + 1):
#     print(chr(i))

# ord("A") == 65
# ord("Z") == 90
# ord("a") == 97
# ord("z") == 122


G, S = map(int, input().split())
w, s = input(), input()

# print(f">>> fun(\"{w}\", \"{s}\")")
print(f"{fun(w, s)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # import random

    # print(ord("a"), ord("z"), chr(97), chr(122))

    # for i in range(1000):
    #     G = random.randint(1, 10)
    #     S = random.randint(G, 100)
    #     w = "".join([chr(random.randint(97, 122)) for _ in range(G)])
    #     s = "".join([chr(random.randint(97, 122)) for _ in range(G)])
    #     if not fun(w, s) == fun2(w, s):
    #         print(f"{w}, {s} \tTrue: {fun2(w, s)}, \tMy: {fun(w, s)}")
