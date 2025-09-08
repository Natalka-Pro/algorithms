"""
Реализуйте бинарное дерево поиска для целых чисел. Программа получает на вход последовательность
целых чисел и строит из них дерево. Элементы в деревья добавляются в соответствии
с результатом поиска их места. Если элемент уже существует в дереве, добавлять его
не надо. Балансировка дерева не производится.

Формат ввода
На вход программа получает последовательность натуральных чисел. Последовательность
завершается числом 0, которое означает конец ввода, и добавлять его в дерево не
надо.

Формат вывода
Выведите единственное число – высоту получившегося дерева.

Пример
Ввод
Вывод
7 3 2 1 9 5 4 6 8 0

4
"""


def depth(tree):

    if tree is None:
        return 0
    else:
        return 1 + max(depth(tree["Left"]), depth(tree["Right"]))


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


def tree2list(tree, l=[]):
    if tree["Right"] is None and tree["Left"] is None:
        return l
    else:

        if tree["Left"] is not None:
            l.append((tree["Key"], tree["Left"]["Key"]))
            l = tree2list(tree["Left"], l)

        if tree["Right"] is not None:
            l.append((tree["Key"], tree["Right"]["Key"]))
            l = tree2list(tree["Right"], l)

        return l


def make_treelib(tree):
    # https://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python
    from anytree import Node, RenderTree

    l = tree2list(tree)

    key2Node = {}
    root = Node(tree["Key"])
    key2Node[tree["Key"]] = root

    for parent_key, child_key in l:
        key2Node[child_key] = Node(child_key, parent=key2Node[parent_key])

    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
    # 7
    # ├── 3
    # │   ├── 2
    # │   │   └── 1
    # │   └── 5
    # │       ├── 4
    # │       └── 6
    # └── 9
    #     └── 8


def fun(s):
    """
    >>> fun([7, 3, 2, 1, 9, 5, 4, 6, 8])
    4
    """

    tree = maketree(s)
    # make_treelib(tree)
    return depth(tree)


s = list(map(int, input().split()))[:-1]
print(fun(s))


# print(f">>> fun({s})")
# print(f"    {fun(s)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
