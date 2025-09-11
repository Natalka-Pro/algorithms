"""
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один
родитель. Каждом элементу дерева сопоставляется целое неотрицательное число, называемое
высотой. У родоначальника высота равна 0, у любого другого элемента высота на 1
больше, чем у его родителя. Вам дано генеалогическое древо, определите высоту всех
его элементов.

Формат ввода
Программа получает на вход число элементов в генеалогическом древе N. Далее следует
N-1 строка, задающие родителя для каждого элемента древа, кроме родоначальника.
Каждая строка имеет вид имя_потомка имя_родителя.

Формат вывода
Программа должна вывести список всех элементов древа в лексикографическом порядке.
После вывода имени каждого элемента необходимо вывести его высоту.

Пример 1
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

Alexander_I 4
Alexei 1
Anna 1
Elizabeth 1
Nicholaus_I 4
Paul_I 3
Peter_I 0
Peter_II 2
Peter_III 2

Пример 2
Ввод
Вывод
10
AQHFYP MKFXCLZBT
AYKOTYQ QIUKGHWCDC
IWCGKHMFM WPLHJL
MJVAURUDN QIUKGHWCDC
MKFXCLZBT IWCGKHMFM
PUTRIPYHNQ UQNGAXNP
QIUKGHWCDC WPLHJL
UQNGAXNP WPLHJL
YURTPJNR QIUKGHWCDC

AQHFYP 3
AYKOTYQ 2
IWCGKHMFM 1
MJVAURUDN 2
MKFXCLZBT 2
PUTRIPYHNQ 2
QIUKGHWCDC 1
UQNGAXNP 1
WPLHJL 0
YURTPJNR 2

Пример 3
Ввод
Вывод
10
BFNRMLH CSZMPFXBZ
CSZMPFXBZ IHWBQDJ
FMVQTU FUXATQUGIG
FUXATQUGIG IRVAVMQKN
GNVIZ IQGIGUJZ
IHWBQDJ LACXYFQHSQ
IQGIGUJZ JMUPNYRQD
IRVAVMQKN GNVIZ
JMUPNYRQD BFNRMLH

BFNRMLH 3
CSZMPFXBZ 2
FMVQTU 9
FUXATQUGIG 8
GNVIZ 6
IHWBQDJ 1
IQGIGUJZ 5
IRVAVMQKN 7
JMUPNYRQD 4
LACXYFQHSQ 0

Примечания
Эта задача имеет решение сложности O(n), но вам достаточно написать решение сложности
O(n2) (не считая сложности обращения к элементам словаря).
Пример ниже соответствует приведенному древу рода Романовых.
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


def depth(root, ans = {}):
    # ans = {Name : depth}

    if root["Parent"] is None:
        ans[root["Name"]] = 0
    
    for child in root["Children"]:
        ans[child["Name"]] = ans[child["Parent"]["Name"]] + 1
        depth(child, ans) 

    return ans


def fun(s):
    """
    >>> fun([['Alexei', 'Peter_I'], ['Anna', 'Peter_I'], ['Elizabeth', 'Peter_I'], ['Peter_II', 'Alexei'], ['Peter_III', 'Anna'], ['Paul_I', 'Peter_III'], ['Alexander_I', 'Paul_I'], ['Nicholaus_I', 'Paul_I']])
    [('Alexander_I', 4), ('Alexei', 1), ('Anna', 1), ('Elizabeth', 1), ('Nicholaus_I', 4), ('Paul_I', 3), ('Peter_I', 0), ('Peter_II', 2), ('Peter_III', 2)]
    >>> fun([['AQHFYP', 'MKFXCLZBT'], ['AYKOTYQ', 'QIUKGHWCDC'], ['IWCGKHMFM', 'WPLHJL'], ['MJVAURUDN', 'QIUKGHWCDC'], ['MKFXCLZBT', 'IWCGKHMFM'], ['PUTRIPYHNQ', 'UQNGAXNP'], ['QIUKGHWCDC', 'WPLHJL'], ['UQNGAXNP', 'WPLHJL'], ['YURTPJNR', 'QIUKGHWCDC']])
    [('AQHFYP', 3), ('AYKOTYQ', 2), ('IWCGKHMFM', 1), ('MJVAURUDN', 2), ('MKFXCLZBT', 2), ('PUTRIPYHNQ', 2), ('QIUKGHWCDC', 1), ('UQNGAXNP', 1), ('WPLHJL', 0), ('YURTPJNR', 2)]
    >>> fun([['BFNRMLH', 'CSZMPFXBZ'], ['CSZMPFXBZ', 'IHWBQDJ'], ['FMVQTU', 'FUXATQUGIG'], ['FUXATQUGIG', 'IRVAVMQKN'], ['GNVIZ', 'IQGIGUJZ'], ['IHWBQDJ', 'LACXYFQHSQ'], ['IQGIGUJZ', 'JMUPNYRQD'], ['IRVAVMQKN', 'GNVIZ'], ['JMUPNYRQD', 'BFNRMLH']])
    [('BFNRMLH', 3), ('CSZMPFXBZ', 2), ('FMVQTU', 9), ('FUXATQUGIG', 8), ('GNVIZ', 6), ('IHWBQDJ', 1), ('IQGIGUJZ', 5), ('IRVAVMQKN', 7), ('JMUPNYRQD', 4), ('LACXYFQHSQ', 0)]
    """

    root = maketree(s)
    # print_tree(root)
    ans = depth(root, {}) # !!! замыкание функции
    ans = sorted(ans.items())

    return ans


N = int(input())
s = [input().split() for _ in range(N-1)]
for name, num in fun(s):
    print(name, num)


# !!! замыкание функции
# def f(x, ans = {}):
#     x = x + 1
#     ans[x] = x + 10
#     print(x)
#     print(ans)

# f(5) # {6: 16}
# f(6) # {6: 16, 7: 17}
    

if __name__ == "__main__":
    import doctest

    doctest.testmod()
