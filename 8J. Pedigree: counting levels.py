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


def fun(s):
    """
    # >>> fun([0, 1, 10, 9])
    # ([0, 1], [9, 10], [3])
    # >>> fun([1, 2])
    # ([2], [1], [3])
    # >>> fun([])
    # ([], [], [])
    """

    return


N, M = map(int, input().split())
s = [int(input()) for _ in range(N)]
print(*fun(s))


# def str2fstr(s):
#     ans = []
#     for i in s:
#         if i.isalpha():
#             ans.append(f"{{{i}}}")
#         else:
#             ans.append(i)
#     return "".join(ans)


# q = "K, s"
# print(f"fun({q})\n>>> fun({str2fstr(q)})")
# print(f">>> fun({str2fstr(q)})".format(*eval(q)))


# print(f">>> fun({s})")
# print(f"    {fun(s)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
