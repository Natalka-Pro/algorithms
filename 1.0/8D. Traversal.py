"""
Выведите все элементы полученного дерева в порядке возрастания.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность
не входит. По данной последовательности требуется построить дерево.

Формат вывода
Выведите ответ на задачу.

Пример
Ввод
Вывод
7 3 2 1 9 5 4 6 8 0

1
2
3
4
5
6
7
8
9
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


def tree_traversal(tree, ans=None):
    # ans = x.copy() # TL
    if ans is None:
        ans = []

    if tree["Left"] is not None:
        ans = tree_traversal(tree["Left"], ans)

    ans.append(tree["Key"])

    if tree["Right"] is not None:
        ans = tree_traversal(tree["Right"], ans)

    return ans


def fun(s):
    """
    >>> fun([7, 3, 2, 1, 9, 5, 4, 6, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    tree = maketree(s)
    return tree_traversal(tree)  # [:len(s)] взлом)))


s = list(map(int, input().split()))[:-1]
# print(fun([7, 3, 2, 1, 9, 5, 4, 6, 8]))
# print(fun([4, 6, 8]))
print(*fun(s), sep="\n")


# print(f">>> fun({s})")
# print(f"    {fun(s)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
