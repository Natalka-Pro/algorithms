"""
Выведите второй по величине элемент в построенном дереве. Гарантируется, что такой
найдется.

Формат ввода
Дана последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность
не входит.

Формат вывода
Выведите ответ на задачу.

Пример
Ввод
Вывод
7 3 2 1 9 5 4 6 8 0

8
"""


def add(tree, item):

    key = tree["Key"]

    if key == item:
        return
    elif key < item:
        if tree["Right"] is None:
            tree["Right"] = {"Key": item, "Left": None, "Right": None}
            return
        else:
            add(tree["Right"], item)
    elif key > item:
        if tree["Left"] is None:
            tree["Left"] = {"Key": item, "Left": None, "Right": None}
            return
        else:
            add(tree["Left"], item)


def maketree(s):
    tree = {"Key": s[0], "Left": None, "Right": None}

    for item in s[1:]:
        add(tree, item)

    return tree


def find_maxs(tree, ans=None):
    # def x(ans=[]):            !!!!!!!!!!!!
    #     ans.append(1)
    #     return ans

    # ans = x.copy()
    if ans is None:
        ans = []

    ans.append(tree["Key"])
    ans.sort()
    if len(ans) > 2:
        ans = ans[1:]

    if tree["Right"] is not None:
        return find_maxs(tree["Right"], ans)
    elif tree["Left"] is not None:
        return find_maxs(tree["Left"], ans)
    else:
        return ans


def fun(s):
    """
    >>> fun([7, 3, 2, 1, 9, 5, 4, 6, 8])
    8
    """
    tree = maketree(s)
    return find_maxs(tree)[0]


def fun2(s):
    """
    >>> fun2([7, 3, 2, 1, 9, 5, 4, 6, 8])
    8
    """

    s = set(s)
    maxs = [s.pop(), s.pop()]

    for i in s:
        maxs.append(i)
        maxs.sort()

        maxs = maxs[1:]

    return maxs[0]


s = list(map(int, input().split()))[:-1]
# print(fun([7, 3, 2, 1, 9, 5, 4, 6, 8]))
# print(fun([7, 3, 2, 1, 9, 5, 4, 6, 8]))
# print(fun([7, 3, 2, 1, 9, 5, 4, 6, 8]))
print(fun(s))

# print(f">>> fun({s})")
# print(f"    {fun(s)}")


# if __name__ == "__main__":
#     import doctest

#     doctest.testmod()
