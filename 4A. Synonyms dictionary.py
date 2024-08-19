"""
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному
ему слову. Все слова в словаре различны. Для одного данного слова определите его
синоним.

Формат ввода
Программа получает на вход количество пар синонимов N. Далее следует N строк, каждая
строка содержит ровно два слова-синонима. После этого следует одно слово.

Формат вывода
Программа должна вывести синоним к данному слову. Примечание
Эту задачу можно решить и без словарей (сохранив все входные данные в списке), но
решение со словарем будет более простым.

Пример 1
Ввод
Вывод
3
Hello Hi
Bye Goodbye
List Array
Goodbye

Bye

Пример 2
Ввод
Вывод
1
beep Car
Car

beep

Пример 3
Ввод
Вывод
2
Ololo Ololo
Numbers 1234567890
Numbers

1234567890

Примечания
Эту задачу можно решить и без словарей (сохранив все входные данные в списке), но
решение со словарем будет более простым.
"""


def fun(s, word):
    """
    >>> fun([('Hello', 'Hi'), ('Bye', 'Goodbye'), ('List', 'Array')], 'Goodbye')
    'Bye'
    >>> fun([('beep', 'Car')], 'Car')
    'beep'
    >>> fun([('Ololo', 'Ololo'), ('Numbers', '1234567890')], 'Numbers')
    '1234567890'
    """

    for i in s:
        if word in i:
            if i[0] == word:
                return i[1]
            else:
                return i[0]


def fun2(s, word):
    """
    >>> fun2([('Hello', 'Hi'), ('Bye', 'Goodbye'), ('List', 'Array')], 'Goodbye')
    'Bye'
    >>> fun2([('beep', 'Car')], 'Car')
    'beep'
    >>> fun2([('Ololo', 'Ololo'), ('Numbers', '1234567890')], 'Numbers')
    '1234567890'
    """

    d = {}
    for w1, w2 in s:
        d[w1] = w2

    for key, value in d.items():
        if key == word:
            return value

        if value == word:
            return key


N = int(input())
s = [tuple(input().split()) for _ in range(N)]
word = input()
print(fun2(s, word))

# print(f">>> fun({s}, {word})")
# print(f"\t{fun(s, word)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
