"""
Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку sys)
записан текст. Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.

Пример
Ввод
Вывод
She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.

19
"""

import sys


def fun(s):
    """
    >>> fun("   She sells sea shells on the sea shore;\
                The shells that she sells are sea shells I'm sure.\
                So if she sells sea shells on the sea shore,\
                I'm sure that the shells are sea shore shells.")
    19
    """

    s = set(s.split())
    return len(s)


print(fun(sys.stdin.read()))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
