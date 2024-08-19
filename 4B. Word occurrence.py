"""
Во входном файле (вы можете читать данные из файла input.txt) записан текст. Словом
считается последовательность непробельных символов идущих подряд, слова разделены
одним или большим числом пробелов или символами конца строки. Для каждого слова
из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.

Пример 1
Ввод
Вывод
one two one tho three

0 0 1 0 0

Пример 2
Ввод
Вывод
She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.

0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0

Пример 3
Ввод
Вывод
aba aba; aba @?"

0 0 1 0
"""

import sys


def fun(s):
    """
    >>> fun("one two one tho three")
    [0, 0, 1, 0, 0]
    >>> fun("She sells sea shells on the sea shore;\
    The shells that she sells are sea shells I'm sure.\
    So if she sells sea shells on the sea shore,\
    I'm sure that the shells are sea shore shells.")
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 2, 2, 0, 0, 0, 0, 1, 2, 3, 3, 1, 1, 4, 0, 1, 0, 1, 2, 4, 1, 5, 0, 0]
    >>> fun("aba aba; aba @?")
    [0, 0, 1, 0]
    """

    d = {}
    ans = []

    for word in s.split():
        if word not in d:
            d[word] = 0

        ans.append(d[word])
        d[word] += 1

    return ans


s = sys.stdin.read()
print(*fun(s))

# print(f">>> fun(\"{s}\")")
# print(f"{fun(s)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
