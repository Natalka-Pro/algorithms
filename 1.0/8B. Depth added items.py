"""
В бинарное дерево поиска добавляются элементы. Выведите глубину для каждого добавленного
элемента в том порядке, как они добавлялись. Если элемент уже есть в дереве, то
ничего добавлять и выводить не нужно. Глубиной называется расстояние от корня дерева
до элемента включительно.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность
не входит. По данной последовательности требуется построить дерево.

Формат вывода
Выведите ответ на задачу.

Пример
Ввод
Вывод
7 3 2 1 9 5 4 6 8 0

1 2 3 4 2 3 4 4 3
"""


def add(tree, item, depth=2):

    key = tree["Key"]

    if key == item:
        return
    elif key < item:
        if tree["Right"] is None:
            tree["Right"] = {"Key": item, "Left": None, "Right": None}
            return depth
        else:
            return add(tree["Right"], item, depth + 1)
    elif key > item:
        if tree["Left"] is None:
            tree["Left"] = {"Key": item, "Left": None, "Right": None}
            return depth
        else:
            return add(tree["Left"], item, depth + 1)


def maketree(s):
    tree = {"Key": s[0], "Left": None, "Right": None}

    ans = [1]
    for item in s[1:]:
        depth = add(tree, item)
        if depth:
            ans.append(depth)

    return tree, ans


def fun(s):
    """
    >>> fun([7, 3, 2, 1, 9, 5, 4, 6, 8])
    [1, 2, 3, 4, 2, 3, 4, 4, 3]
    >>> fun([7, 3, 2, 1, 9, 5, 4, 6, 8, 7, 3, 2, 1])
    [1, 2, 3, 4, 2, 3, 4, 4, 3]
    """

    tree, ans = maketree(s)
    return ans


def find_depth(elem, tree, depth=1):
    if tree is None:
        return 0
    elif tree["Key"] == elem:
        return depth
    else:
        dl = find_depth(elem, tree["Left"], depth + 1)

        dr = find_depth(elem, tree["Right"], depth + 1)

        return max(dl, dr)


def fun2(s):
    """
    TL - 41 test

    >>> fun2([7, 3, 2, 1, 9, 5, 4, 6, 8])
    [1, 2, 3, 4, 2, 3, 4, 4, 3]
    >>> fun2([7, 3, 2, 1, 9, 5, 4, 6, 8, 7, 3, 2, 1])
    [1, 2, 3, 4, 2, 3, 4, 4, 3]
    """

    tree, ans = maketree(s)

    ans = []
    ans_set = set()
    for i, item in enumerate(s):
        if item not in ans_set:
            ans.append(find_depth(item, tree))
            ans_set.add(item)

    return ans


s = list(map(int, input().split()))[:-1]
# print(fun([7, 3, 2, 1, 9, 5, 4, 6, 8]))
print(*fun(s))


# print(f">>> fun({s})")
# print(f"    {fun(s)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
