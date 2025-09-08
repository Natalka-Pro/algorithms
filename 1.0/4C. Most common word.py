"""
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких
слов несколько, выведите то, которое меньше в лексикографическом порядке.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.

Пример 1
Ввод
Вывод
apple orange banana banana orange

banana

Пример 2
Ввод
Вывод
oh you touch my tralala mmm my ding ding dong

ding

Пример 3
Ввод
Вывод
q w e r t y u i o p
a s d f g h j k l
z x c v b n m

a
"""

import sys


def fun(s):
    """
    >>> fun("apple orange banana banana orange")
    'banana'
    >>> fun("oh you touch my tralala mmm my ding ding dong")
    'ding'
    >>> fun("q w e r t y u i o p\
    a s d f g h j k l\
    z x c v b n m")
    'a'
    """

    d = {}

    for word in s.split():
        if word not in d:
            d[word] = 0

        d[word] += 1

    l = [(-val, key) for key, val in d.items()]
    return min(l)[1]


s = sys.stdin.read()
print(fun(s))

# print(f">>> fun(\"{s}\")")
# print(f"{fun(s)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
