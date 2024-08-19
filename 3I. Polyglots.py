"""
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки
знают все школьники и языки, которые знает хотя бы один из школьников.

Формат ввода
Первая строка входных данных содержит количество школьников N. Далее идет N чисел
Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает
i-й школьник. Длина названий языков не превышает 1000 символов, количество различных
языков не более 1000. 1 ≤ N ≤ 1000, 1 ≤ Mi ≤ 500.

Формат вывода
В первой строке выведите количество языков, которые знают все школьники. Начиная
со второй строки - список таких языков. Затем - количество языков, которые знает
хотя бы один школьник, на следующих строках - список таких языков.

Пример
Ввод
Вывод
3
3
Russian
English
Japanese
2
Russian
English
1
English

1
English
3
Russian
Japanese
English
"""


def fun(s):
    """
    >>> fun([['Russian', 'English', 'Japanese'], ['Russian', 'English'], ['English']])
    (['English'], ['English', 'Japanese', 'Russian'])
    """

    all = set(s[0])
    one = set()

    for lang in s:
        lang = set(lang)
        all &= lang
        one |= lang

    return sorted(all), sorted(one)


N = int(input())
s = []
for _ in range(N):
    M = int(input())
    s.append([input() for i in range(M)])


ans = fun(s)
for i in ans:
    print(len(i), *i, sep="\n")

# print(f">>> fun({s})")
# print(f"{fun(s)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
