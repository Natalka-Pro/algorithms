"""
Дерево называется АВЛ-сбалансированным, если для любой его вершины высота левого
и правого поддерева для этой вершины различаются не более чем на 1.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность
не входит. Постройте дерево, соответствующее данной последовательности.

Формат вывода
Определите, является ли дерево сбалансированным, выведите слово YES или NO.

Пример
Ввод
Вывод
7 3 2 1 9 5 4 6 8 0

YES
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


def avl(tree):

    if tree is None:
        return True, 0

    left_avl, left_height = avl(tree["Left"])
    right_avl, right_height = avl(tree["Right"])

    cur_height = max(left_height, right_height) + 1
    # print(tree["Key"], cur_height)

    if left_avl and right_avl and abs(right_height - left_height) <= 1:
        return True, cur_height
    else:
        return False, cur_height


def fun(s):
    """
    >>> fun([7, 3, 2, 1, 9, 5, 4, 6, 8])
    'YES'
    >>> fun([1])
    'YES'
    >>> fun([1, 2, 3])
    'NO'
    """

    tree = maketree(s)

    return "YES" if avl(tree)[0] else "NO"


s = list(map(int, input().split()))[:-1]
# fun([7, 3, 2, 1, 9, 5, 4, 6, 8])
print(fun(s))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
