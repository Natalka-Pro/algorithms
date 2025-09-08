"""
Дано N отрезков провода длиной L1, L2, ..., LN сантиметров. Требуется с помощью
разрезания получить из них K равных отрезков как можно большей длины, выражающейся
целым числом сантиметров. Если нельзя получить K отрезков длиной даже 1 см, вывести
0.

Формат ввода
В первой строке находятся числа N и К. В следующих N строках - L1, L2, ..., LN,
по одному числу в строке.
Ограничения: 1 ≤ N, K ≤ 10 000, 100 ≤ Li ≤ 10 000 000, все числа целые.

Формат вывода
Вывести одно число - полученную длину отрезков.

Пример
Ввод
Вывод
4 11
802
743
457
539

200
"""


def num_seg(L, max_len):
    ans = 0
    for i in L:
        ans += i // max_len

    return ans


def check(max_len, params):
    L, K = params
    return num_seg(L, max_len) >= K


def rfind(l, r, params):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, params):
            l = m
        else:
            r = m - 1

    return l


def fun(L, K):
    """
    >>> fun([802, 743, 457, 539], 11)
    200
    """

    return rfind(0, max(L), (L, K))


N, K = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(fun(L, K))


# def str2fstr(s):
#     ans = []
#     for i in s:
#         if i.isalpha():
#             ans.append(f"{{}}")
#         else:
#             ans.append(i)
#     return "".join(ans)


# print(f">>> fun({str2fstr('L, K')})".format(L, K))
# print(f"    {fun(L, K)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
