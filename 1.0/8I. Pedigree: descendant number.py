"""
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один
родитель.
Для каждого элемента дерева определите число всех его потомков (не считая его самого).

Формат ввода
Программа получает на вход число элементов в генеалогическом древе N. Далее следует
N−1 строка, задающие родителя для каждого элемента древа, кроме родоначальника.
Каждая строка имеет вид имя_потомка имя_родителя.

Формат вывода
Выведите список всех элементов в лексикографическом порядке, для каждого элемента
выводите количество всех его потомков.

Пример
Ввод
Вывод
9
Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I

Alexander_I 0
Alexei 1
Anna 4
Elizabeth 0
Nicholaus_I 0
Paul_I 2
Peter_I 8
Peter_II 0
Peter_III 3

Примечания
Если вы используете рекурсию, то вам может быть полезно добавление в начало программы
следующих строк:
import sys
sys.setrecursionlimit(100000)
"""

import sys

sys.setrecursionlimit(100000)


def maketree(s):
    nodes = {}

    for child, parent in s:

        if child not in nodes:
            nodes[child] = {"Name" : child, "Parent" : None, "Children" : []}

        if parent not in nodes:
            nodes[parent] = {"Name" : parent, "Parent" : None, "Children" : []}

        # nodes[child]["Parent"] = parent
        # nodes[parent]["Children"].append(child)
        nodes[child]["Parent"] = nodes[parent]
        nodes[parent]["Children"].append(nodes[child])


    for val in nodes.values():
        if val["Parent"] is None:
            return val

    raise TypeError("Cycle in tree!!!")


def print_tree(root, level=0):
    print("\t" * level + root["Name"])

    for child in root["Children"]:
        print_tree(child, level+1)


def num_descendant(root, ans = {}):
    # ans = {Name : num descendants}
    num = 0
    for child in root["Children"]:
        num += num_descendant(child, ans)[child["Name"]] + 1

    ans[root["Name"]] = num
    return ans


def fun(s):
    """
    >>> fun([['Alexei', 'Peter_I'], ['Anna', 'Peter_I'], ['Elizabeth', 'Peter_I'], ['Peter_II', 'Alexei'], ['Peter_III', 'Anna'], ['Paul_I', 'Peter_III'], ['Alexander_I', 'Paul_I'], ['Nicholaus_I', 'Paul_I']])
    [('Alexander_I', 0), ('Alexei', 1), ('Anna', 4), ('Elizabeth', 0), ('Nicholaus_I', 0), ('Paul_I', 2), ('Peter_I', 8), ('Peter_II', 0), ('Peter_III', 3)]
    """

    root = maketree(s)
    # print_tree(root)
    ans = num_descendant(root, {}) # !!! замыкание функции
    ans = sorted(ans.items())

    return ans


N = int(input())
s = [input().split() for _ in range(N-1)]
for name, num in fun(s):
    print(name, num)

# fun([['Alexei', 'Peter_I'], ['Anna', 'Peter_I'], ['Elizabeth', 'Peter_I'], ['Peter_II', 'Alexei'], ['Peter_III', 'Anna'], ['Paul_I', 'Peter_III'], ['Alexander_I', 'Paul_I'], ['Nicholaus_I', 'Paul_I']])
# fun([['AQHFYP', 'MKFXCLZBT'], ['AYKOTYQ', 'QIUKGHWCDC'], ['IWCGKHMFM', 'WPLHJL'], ['MJVAURUDN', 'QIUKGHWCDC'], ['MKFXCLZBT', 'IWCGKHMFM'], ['PUTRIPYHNQ', 'UQNGAXNP'], ['QIUKGHWCDC', 'WPLHJL'], ['UQNGAXNP', 'WPLHJL'], ['YURTPJNR', 'QIUKGHWCDC']])
    

# print(fun([['Alexei', 'Peter_I'], ['Anna', 'Peter_I'], 
#            ['Elizabeth', 'Peter_I'], ['Peter_II', 'Alexei'], 
#            ['Peter_III', 'Anna'], ['Paul_I', 'Peter_III'], 
#            ['Alexander_I', 'Paul_I'], ['Nicholaus_I', 'Paul_I']]))

# print(f">>> fun({s})")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
