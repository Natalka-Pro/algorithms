"""
Некоторый банк хочет внедрить систему управления счетами клиентов, поддерживающую
следующие операции:
Пополнение счета клиента.
Снятие денег со счета.
Запрос остатка средств на счете.
Перевод денег между счетами клиентов.
Начисление процентов всем клиентам.
Вам необходимо реализовать такую систему. Клиенты банка идентифицируются именами
(уникальная строка, не содержащая пробелов). Первоначально у банка нет ни одного
клиента. Как только для клиента проводится операция пололнения, снятия или перевода
денег, ему заводится счет с нулевым балансом. Все дальнейшие операции проводятся
только с этим счетом. Сумма на счету может быть как положительной, так и отрицательной,
при этом всегда является целым числом.

Формат ввода
Входной файл содержит последовательность операций. Возможны следующие операции:
DEPOSIT name sum - зачислить сумму sum на счет клиента name. Если у клиента нет
счета, то счет создается. WITHDRAW name sum - снять сумму sum со счета клиента name.
Если у клиента нет счета, то счет создается. BALANCE name - узнать остаток средств
на счету клиента name. TRANSFER name1 name2 sum - перевести сумму sum со счета клиента
name1 на счет клиента name2. Если у какого-либо клиента нет счета, то ему создается
счет. INCOME p - начислить всем клиентам, у которых открыты счета, p% от суммы счета.
Проценты начисляются только клиентам с положительным остатком на счету, если у клиента
остаток отрицательный, то его счет не меняется. После начисления процентов сумма
на счету остается целой, то есть начисляется только целое число денежных единиц.
Дробная часть начисленных процентов отбрасывается.

Формат вывода
Для каждого запроса BALANCE программа должна вывести остаток на счету данного клиента.
Если же у клиента с запрашиваемым именем не открыт счет в банке, выведите ERROR.

Пример 1
Ввод
Вывод
DEPOSIT Ivanov 100
INCOME 5
BALANCE Ivanov
TRANSFER Ivanov Petrov 50
WITHDRAW Petrov 100
BALANCE Petrov
BALANCE Sidorov

105
-50
ERROR

Пример 2
Ввод
Вывод
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 100
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 150
BALANCE Petrov
DEPOSIT Ivanov 10
DEPOSIT Petrov 15
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 46
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 14
BALANCE Ivanov
BALANCE Petrov

ERROR
ERROR
100
ERROR
150
110
165
156
165
156
179

Пример 3
Ввод
Вывод
BALANCE a
BALANCE b
DEPOSIT a 100
BALANCE a
BALANCE b
WITHDRAW a 20
BALANCE a
BALANCE b
WITHDRAW b 78
BALANCE a
BALANCE b
WITHDRAW a 784
BALANCE a
BALANCE b
DEPOSIT b 849
BALANCE a
BALANCE b

ERROR
ERROR
100
ERROR
80
ERROR
80
-78
-704
-78
-704
771
"""

import sys


def fun(s):
    """
    >>> fun("   DEPOSIT Ivanov 100\\n\
                INCOME 5\\n\
                BALANCE Ivanov\\n\
                TRANSFER Ivanov Petrov 50\\n\
                WITHDRAW Petrov 100\\n\
                BALANCE Petrov\\n\
                BALANCE Sidorov")
    >>> fun("   BALANCE Ivanov\\n\
                BALANCE Petrov\\n\
                DEPOSIT Ivanov 100\\n\
                BALANCE Ivanov\\n\
                BALANCE Petrov\\n\
                DEPOSIT Petrov 150\\n\
                BALANCE Petrov\\n\
                DEPOSIT Ivanov 10\\n\
                DEPOSIT Petrov 15\\n\
                BALANCE Ivanov\\n\
                BALANCE Petrov\\n\
                DEPOSIT Ivanov 46\\n\
                BALANCE Ivanov\\n\
                BALANCE Petrov\\n\
                DEPOSIT Petrov 14\\n\
                BALANCE Ivanov\\n\
                BALANCE Petrov")
    ['ERROR', 'ERROR', 100, 'ERROR', 150, 110, 165, 156, 165, 156, 179]
    >>> fun("   BALANCE a\\n\
                BALANCE b\\n\
                DEPOSIT a 100\\n\
                BALANCE a\\n\
                BALANCE b\\n\
                WITHDRAW a 20\\n\
                BALANCE a\\n\
                BALANCE b\\n\
                WITHDRAW b 78\\n\
                BALANCE a\\n\
                BALANCE b\\n\
                WITHDRAW a 784\\n\
                BALANCE a\\n\
                BALANCE b\\n\
                DEPOSIT b 849\\n\
                BALANCE a\\n\
                BALANCE b")
    ['ERROR', 'ERROR', 100, 'ERROR', 80, 'ERROR', 80, -78, -704, -78, -704, 771]
    """

    d = {}
    ans = []

    for stroke in s.strip().split("\n"):
        command = stroke.split()

        match command[0]:
            case "DEPOSIT":

                name, sum = command[1:]
                sum = int(sum)

                if name not in d:
                    d[name] = 0
                d[name] += sum

            case "WITHDRAW":
                name, sum = command[1:]
                sum = int(sum)

                if name not in d:
                    d[name] = 0
                d[name] -= sum

            case "BALANCE":
                name = command[1]

                if name in d:
                    ans.append(d[name])
                else:
                    ans.append("ERROR")

            case "TRANSFER":
                name1, name2, sum = command[1:]
                sum = int(sum)

                if name1 not in d:
                    d[name1] = 0

                if name2 not in d:
                    d[name2] = 0

                d[name1] -= sum
                d[name2] += sum

            case "INCOME":
                p = command[1]
                p = int(p)
                p = 1 + p / 100

                for name, value in d.items():
                    if value > 0:
                        d[name] = int(value * p)

    return ans


s = sys.stdin.read()
print(*fun(s), sep="\n")


# s1 = s.strip().replace("\n", "\\\\n\\\n")
# print(f">>> fun(\"{s1}\")")
# print(f"{fun(s)}")


# if __name__ == "__main__":
#     import doctest

#     doctest.testmod()
