"""
По последовательности чисел во входных данных определите ее вид:
CONSTANT – последовательность состоит из одинаковых значений
ASCENDING – последовательность является строго возрастающей
WEAKLY ASCENDING – последовательность является нестрого возрастающей
DESCENDING – последовательность является строго убывающей
WEAKLY DESCENDING – последовательность является нестрого убывающей
RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов

Формат ввода
По одному на строке поступают числа последовательности ai, |ai| ≤ 109.
Признаком окончания последовательности является число -2× 109. Оно в последовательность
не входит.

Формат вывода
В единственной строке выведите тип последовательности.

Пример
Ввод
Вывод
-530
-530
-530
-530
-530
-530
-2000000000

CONSTANT
"""


def fun(s):
    """
    >>> fun([-530, -530, -530, -530, -530, -530])
    'CONSTANT'
    >>> fun([1, 1, 2, 3, 4])
    'WEAKLY ASCENDING'
    >>> fun([-1, -1, -2, -3, -4])
    'WEAKLY DESCENDING'
    """
    ans = "CONSTANT"

    for i in range(len(s) - 1):

        match ans:
            case "CONSTANT":
                if s[i] < s[i + 1]:
                    if i == 0:
                        ans = "ASCENDING"
                    else:
                        ans = "WEAKLY ASCENDING"
                elif s[i] > s[i + 1]:
                    if i == 0:
                        ans = "DESCENDING"
                    else:
                        ans = "WEAKLY DESCENDING"

            case "ASCENDING":
                if s[i] == s[i + 1]:
                    ans = "WEAKLY ASCENDING"
                elif s[i] > s[i + 1]:
                    ans = "RANDOM"

            case "DESCENDING":
                if s[i] == s[i + 1]:
                    ans = "WEAKLY DESCENDING"
                elif s[i] < s[i + 1]:
                    ans = "RANDOM"

            case "WEAKLY ASCENDING":
                if s[i] > s[i + 1]:
                    ans = "RANDOM"

            case "WEAKLY DESCENDING":
                if s[i] < s[i + 1]:
                    ans = "RANDOM"

    return ans


eos = -2e9
s = []
while (x := int(input())) != eos:
    s.append(x)

print(fun(s))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
