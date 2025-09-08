"""
Для полученного дерева выведите список всех листьев (вершин, не имеющих потомков)
в порядке возрастания.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность
не входит.

Формат вывода
Выведите ответ на задачу.

Пример
Ввод
Вывод
7 3 2 1 9 5 4 6 8 0

1
4
6
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


def leaf_traversal(tree, ans=None):
    if ans is None:
        ans = []

    if tree["Left"] is not None:
        ans = leaf_traversal(tree["Left"], ans)

    if tree["Right"] is not None:
        ans = leaf_traversal(tree["Right"], ans)

    if tree["Left"] is None and tree["Right"] is None:
        ans.append(tree["Key"])

    return ans


def fun(s):
    """
    >>> fun([7, 3, 2, 1, 9, 5, 4, 6, 8])
    [1, 4, 6, 8]
    """
    tree = maketree(s)
    return leaf_traversal(tree)


s = list(map(int, input().split()))[:-1]
# print(fun([7, 3, 2, 1, 9, 5, 4, 6, 8]))
print(*fun(s), sep="\n")


# print(f">>> fun({s})")
# print(f"    {fun(s)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
