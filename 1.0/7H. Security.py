"""
На секретной военной базе работает N охранников. Сутки поделены на 10000 равных
промежутков времени, и известно когда каждый из охранников приходит на дежурство
и уходит с него. Например, если охранник приходит в 5, а уходит в 8, то значит,
что он был в 6, 7 и 8-ой промежуток (а в 5-й нет!!!).
Укажите, верно ли что для данного набора охранников, объект охраняется в любой момент
времени хотя бы одним охранником и удаление любого из них приводит к появлению промежутка
времени, когда объект не охраняется.

Формат ввода
В первой строке входного файла записано натуральное число K (1 ≤ K ≤ 100) — количество
тестов в файле. Каждый тест начинается с числа N (1 ≤ N ≤ 10000), за которым следует
N пар неотрицательных целых чисел A и B — время прихода на дежурство и ухода (0 ≤ A ≤ B ≤ 10000)
соответствующего охранника.

Формат вывода
Выведите K строк, где в M-ой строке находится слово Accepted, если M-ый набор охранников
удовлетворяет описанным выше условиям. В противном случае выведите Wrong Answer.

Пример
Ввод
Вывод
2
3 0 3000 2500 7000 2700 10000
2 0 3000 2700 10000

Wrong Answer
Accepted
"""

IN = 0
OUT = 1


def fun(s):
    """
    >>> fun([[0, 3000], [2500, 7000], [2700, 10000]])
    False
    >>> fun([[0, 3000], [2700, 10000]])
    True
    >>> fun([[0, 3000], [3000, 10000]])
    True
    >>> fun([[0, 3000], [3000, 7000], [7000, 10000]])
    True
    >>> fun([[0, 2], [2, 3], [4, 10000]])
    False
    >>> fun([[0, 2], [1, 3], [2, 10000]])
    False
    """

    events = []

    for person, (x, y) in enumerate(s):
        if x < y:
            events.append((x, IN, person))

            events.append((y, OUT, person))

    events.sort()
    # print(events)

    if events[0][0] != 0 or events[-1][0] != 10000:
        # print("!!!!!!!")
        return False

    num = 0
    current_persons = set()  # кто сейчас охранник

    only_one = [False] * len(s)
    # каждый охранник должен в какой-то момент времени быть один

    prev_time = 0

    for time, type, person in events:

        if time != prev_time:  # ненулевое время прошло
            if num == 1:  # в current_persons один элемент
                elem = current_persons.pop()
                current_persons.add(elem)

                only_one[elem] = True
            elif num == 0 and time != 10000:
                # print("!!!!", time, type, person)
                return False

        if type == IN:
            num += 1
            current_persons.add(person)

        if type == OUT:
            num -= 1
            current_persons.remove(person)

        prev_time = time
        # print((time, type), num, current_persons, only_one, prev_time)

    for elem in only_one:
        if not elem:
            return False
    else:
        return True


K = int(input())

# ML - 15 test
# s = []
# for _ in range(K):
#     x = list(map(int, input().split()))
#     num, *x = x
#     elem = []
#     for i in range(num):
#         elem.append(x[2 * i : 2 * i + 2])
#     s.append(elem)

# for elem in s:
#     # print(f">>> fun({elem})")
#     print("Accepted" if fun(elem) else "Wrong Answer")


for _ in range(K):
    x = list(map(int, input().split()))
    num, *x = x
    elem = []
    for i in range(num):
        elem.append(x[2 * i : 2 * i + 2])
    print("Accepted" if fun(elem) else "Wrong Answer")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
