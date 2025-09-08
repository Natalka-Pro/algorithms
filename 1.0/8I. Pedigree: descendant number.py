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
