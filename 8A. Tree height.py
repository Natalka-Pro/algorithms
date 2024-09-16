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
    # elif tree["Right"] is None:
    #     return 1 + depth(tree["Left"])
    # elif tree["Left"] is None:
    #     return 1 + depth(tree["Right"])
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


# def make_treelib(tree):
#     from anytree import Node, RenderTree

#     udo = Node("Udo")
#     marc = Node("Marc", parent=udo)
#     lian = Node("Lian", parent=marc)
#     dan = Node("Dan", parent=udo)
#     jet = Node("Jet", parent=dan)
#     jan = Node("Jan", parent=dan)
#     joe = Node("Joe", parent=dan)

#     print(udo)
#     Node('/Udo')
#     print(joe)
#     Node('/Udo/Dan/Joe')

#     for pre, fill, node in RenderTree(udo):
#         print("%s%s" % (pre, node.name))
#     # Udo
#     # ├── Marc
#     # │   └── Lian
#     # └── Dan
#     #     ├── Jet
#     #     ├── Jan
#     #     └── Joe

#     print(dan.children)
#     (Node('/Udo/Dan/Jet'), Node('/Udo/Dan/Jan'), Node('/Udo/Dan/Joe'))


def fun(s):
    """
    >>> fun([7, 3, 2, 1, 9, 5, 4, 6, 8])
    4
    """

    tree = {"Key": s[0], "Left": None, "Right": None}

    for item in s[1:]:
        add(tree, item)

    return depth(tree)


s = list(map(int, input().split()))[:-1]
print(fun(s))


# print(f">>> fun({s})")
# print(f"    {fun(s)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
