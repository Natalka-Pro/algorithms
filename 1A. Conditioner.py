"""
В офисе, где работает программист Петр, установили кондиционер нового типа. Этот
кондиционер отличается особой простотой в управлении. У кондиционера есть всего
лишь два управляемых параметра: желаемая температура и режим работы.
Кондиционер может работать в следующих четырех режимах:
«freeze» — охлаждение. В этом режиме кондиционер может только уменьшать температуру.
Если температура в комнате и так не больше желаемой, то он выключается.
«heat» — нагрев. В этом режиме кондиционер может только увеличивать температуру.
Если температура в комнате и так не меньше желаемой, то он выключается.
«auto» — автоматический режим. В этом режиме кондиционер может как увеличивать,
так и уменьшать температуру в комнате до желаемой.
«fan» — вентиляция. В этом режиме кондиционер осуществляет только вентиляцию воздуха
и не изменяет температуру в комнате.
Кондиционер достаточно мощный, поэтому при настройке на правильный режим работы
он за час доводит температуру в комнате до желаемой.
Требуется написать программу, которая по заданной температуре в комнате troom, установленным
на кондиционере желаемой температуре tcond и режиму работы определяет температуру,
которая установится в комнате через час.

Формат ввода
Первая строка входного файла содержит два целых числа troom, и tcond, разделенных
ровно одним пробелом (–50 ≤ troom ≤ 50, –50 ≤ tcond ≤ 50).
Вторая строка содержит одно слово, записанное строчными буквами латинского алфавита
— режим работы кондиционера.

Формат вывода
Выходной файл должен содержать одно целое число — температуру, которая установится
в комнате через час.

Пример 1
Ввод
Вывод
10 20
heat

20

Пример 2
Ввод
Вывод
10 20
freeze

10

Примечания
В первом примере кондиционер находится в режиме нагрева. Через час он нагреет комнату
до желаемой температуры в 20 градусов.
Во втором примере кондиционер находится в режиме охлаждения. Поскольку температура
в комнате ниже, чем желаемая, кондиционер самостоятельно выключается и температура
в комнате не поменяется.
"""


def fun(t_room, t_cond, mode):
    """
    >>> fun(10, 20, 'heat')
    20
    >>> fun(10, 20, 'freeze')
    10
    """
    match mode:
        case "freeze":
            if t_cond >= t_room:
                return t_room
            else:
                return t_cond
        case "heat":
            if t_cond <= t_room:
                return t_room
            else:
                return t_cond
        case "auto":
            return t_cond
        case "fan":
            return t_room


# заданной температуре в комнате troom,
# установленным на кондиционере желаемой температуре tcond
t_room, t_cond = map(int, input().split())
mode = input()

print(fun(t_room, t_cond, mode))

if __name__ == "__main__":
    import doctest

    doctest.testmod()