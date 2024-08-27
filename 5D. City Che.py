"""
В центре города Че есть пешеходная улица - одно из самых популярных мест для прогулок
жителей города. По этой улице очень приятно гулять, ведь вдоль улицы расположено
n забавных памятников.
Девочке Маше из города Че нравятся два мальчика из ее школы, и она никак не может
сделать выбор между ними. Чтобы принять окончательное решение, она решила назначить
обоим мальчикам свидание в одно и то же время. Маша хочет выбрать два памятника
на пешеходной улице, около которых мальчики будут ее ждать. При этом она хочет выбрать
такие памятники, чтобы мальчики не увидели друг друга. Маша знает, что из-за тумана
мальчики увидят друг друга только в том случае, если они будут на расстоянии не
более r метров.
Маше заинтересовалась, а сколько способов есть выбрать два различных памятника для
организации свиданий.

Формат ввода
В первой строке входного файла находятся два целых числа n и r (2 ≤ n ≤ 300000,
1 ≤ r ≤ 109) - количество памятников и максимальное расстояние, на котором мальчики
могут увидеть друг друга.
Во второй строке задано n положительных чисел d1, …, dn, где di - расстояние от
i-го памятника до начала улицы. Все памятники находятся на разном расстоянии от
начала улицы. Памятники приведены в порядке возрастания расстояния от начала улицы
(1 ≤ d1, d2, …, dn ≤ 109).

Формат вывода
Выведите одно число - число способов выбрать два памятника для организации свиданий.

Пример
Ввод
Вывод
4 4
1 3 5 8

2

Примечания
В приведенном примере Маша может выбрать памятники 1 и 4 или памятники 2 и 4.
"""


def fun(s, r):
    """
    >>> fun([1, 3, 5, 8], 4)
    2
    """

    right = 0
    ans = 0
    for left in range(len(s) - 1):
        while right < len(s) and abs(s[right] - s[left]) <= r:
            right += 1

        if right < len(s):
            ans += len(s) - right
            # print(len(s) - right, s[left], s[right])

    return ans


n, r = map(int, input().split())
s = list(map(int, input().split()))
print(fun(s, r))

# print(f">>> fun({s}, {r})")
# print(f"{fun(s, r)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
