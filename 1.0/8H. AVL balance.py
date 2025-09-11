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


def height(tree):
    if tree is None:
        return 0

    h = max(height(tree["Left"]), height(tree["Right"])) + 1
    tree["height"] = h
    return h


def avl(tree):
    height(tree)  # заполним height
    # print(tree)

    if tree is None:
        return True

    left_height = tree["Left"]["height"] if tree["Left"] is not None else 0
    right_height = tree["Right"]["height"] if tree["Right"] is not None else 0

    if abs(right_height - left_height) <= 1:
        return avl(tree["Left"]) and avl(tree["Right"])
    else:
        return False


def fun(s):
    """
    >>> fun([7, 3, 2, 1, 9, 5, 4, 6, 8])
    'YES'
    >>> fun([1])
    'YES'
    """

    tree = maketree(s)

    return "YES" if avl(tree) else "NO"


s = list(map(int, input().split()))[:-1]
# fun([7, 3, 2, 1, 9, 5, 4, 6, 8])
print(fun(s))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
