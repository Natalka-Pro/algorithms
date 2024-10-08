"""
Преподаватель курса ОиМП заказал у одного известного психолога полное психологическое
обследование всех студентов, поступивших на ФНК с целью выяснить их склонность к
списыванию еще до начала занятий и отчислить их за списывание еще до того как они
приступят к занятиям и смогут позорить ФНК своими преступлениями. Психолог, привлеченный
для проведения обследования, известен своим инновационным методом, позволяющим понять
склонность к списыванию студента по наиболее часто используемому им в программах
идентификатору. Помогите известному психологу определить, какие из студентов потенциально
являются преступниками. Напишите программу, которая по приведенной программе выяснит
наиболее часто используемый в ней идентификатор.
Поскольку разные студенты на тестировании пишут программы на разных языках программирования,
ваша программа должна уметь работать с произвольным языком. Поскольку в разных языках
используются различные ключевые слова, то список ключевых слов в анализируемом языке
предоставляется на вход программе. Все последовательности из латинских букв, цифр
и знаков подчеркивания, которые не являются ключевыми словами и содержат хотя бы
один символ, не являющийся цифрой, могут быть идентификаторами. При этом в некоторых
языках идентификаторы могут начинаться с цифры, а в некоторых - нет. Если идентификатор
не может начинаться с цифры, то последовательность, начинающаяся с цифры, идентификатором
не является. Кроме этого, задано, является ли язык чувствительным к регистру символов,
используемых в идентификаторах и ключевых словах.

Формат ввода
В первой строке вводятся число n - количество ключевых слов в языке (0 <= n <= 50)
и два слова C и D, каждое из которых равно либо "yes", либо "no". Слово C равно
"yes", если идентификаторы и ключевые слова в языке чувствительны к регистру символов,
и "no", если нет. Слово D равно "yes", если идентификаторы в языке могут начинаться
с цифры, и "no", если нет.
Следующие n строк содержат по одному слову, состоящему из букв латинского алфавита
и символов подчеркивания - ключевые слова. Все ключевые слова непусты, различны,
при этом, если язык не чувствителен к регистру, то различны и без учета регистра.
Длина каждого ключевого слова не превышает 50 символов.
Далее до конца входных данных идет текст программы. Он содержит только символы с
ASCII-кодами от 32 до 126 и переводы строки.
Размер входных данных не превышает 10 килобайт. В программе есть хотя бы один идентификатор.

Формат вывода
Выведите идентификатор, встречающийся в программе максимальное число раз. Если таких
идентификаторов несколько, следует вывести тот, который встречается в первый раз
раньше. Если язык во входных данных не чувствителен к регистру, то можно выводить
идентификатор в любом регистре.

Пример 1
Ввод
Вывод
0 yes no
int main() {
int a;
int b;
scanf("%d%d", &a, &b);
printf("%d", a + b);
}

int

Пример 2
Ввод
Вывод
0 yes no
#define INT int
int main() {
INT a, b;
scanf("%d%d", &a, &b);
printf("%d %d", a + b, 0);
}

d

Пример 3
Ввод
Вывод
6 no no
program
var
begin
end
while
for
program sum;
var
A, B: integer;
begin
read(A, b);
writeln(a + b);
end.

a

Пример 4
Ввод
Вывод
1 yes yes
_
a = 0h
b = 0h
c = 0h

0h
"""

# def isidentifier(word, StartDigits):
#     if word.isdigit():
#         return False

#     if not StartDigits and 48 <= ord(word[0]) <= 57:
#         return False

#     for w in word:
#         o = ord(w)
#         if not (w == "_" or 48 <= o <= 57 or 65 <= o <= 90 or 97 <= o <= 122):
#             return False

#     return True


# def only_ok(word):
#     ans = []

#     cur = []
#     for s in word:
#         o = ord(s)
#         if s == "_" or 48 <= o <= 57 or 65 <= o <= 90 or 97 <= o <= 122:
#             cur.append(s)
#         elif len(cur) != 0:
#             ans.append("".join(cur))
#             cur = []

#     if len(cur) != 0:
#         ans.append("".join(cur))

#     return ans

import sys


def isidentifier(word, StartDigits):
    if word.isdigit():
        return False

    if not StartDigits and word[0].isdigit():
        return False

    return True


def only_ok(word):
    ans = []
    for w in word:
        if w == "_" or w.isdigit() or w.isalpha():
            ans.append(w)
        else:
            ans.append(" ")

    return "".join(ans)


def fun(keywords, program, CaseSens, StartDigits):
    """
    >>> fun([], "   int main() {\
                    int a;\
                    int b;\
                    scanf('%d%d', &a, &b);\
                    printf('%d', a + b);\
                    }", "yes", "no")
    'int'
    >>> fun([], "   #define INT int\
                    int main() {\
                    INT a, b;\
                    scanf('%d%d', &a, &b);\
                    printf('%d %d', a + b, 0);\
                    }", "yes", "no")
    'd'
    >>> fun(['program', 'var', 'begin', 'end', 'while', 'for'],\
            "   program sum;\
                var\
                A, B: integer;\
                begin\
                read(A, b);\
                writeln(a + b);\
                end.", "no", "no")
    'a'
    >>> fun(['_'], "a = 0h\
                    b = 0h\
                    c = 0h", "yes", "yes")
    '0h'
    """

    CaseSens = CaseSens == "yes"
    StartDigits = StartDigits == "yes"

    program = program.split()

    if CaseSens:
        keywords = set(keywords)
    else:
        keywords = {i.lower() for i in keywords}

    c = {}

    word_number = 0
    for line in program:

        words = only_ok(line).split()

        for word in words:
            if not CaseSens:
                word = word.lower()

            if word not in keywords and isidentifier(word, StartDigits):
                if word not in c:
                    c[word] = [0, word_number]
                    word_number += 1

                c[word][0] += 1

    max_count = 0
    max_idx = 0
    ans = None

    for key, value in c.items():
        count, idx = value

        if count > max_count or (count == max_count and idx < max_idx):
            max_count = count
            max_idx = idx
            ans = key

    return ans


n, C, D = input().split()
n = int(n)
keywords = [input() for _ in range(n)]
program = sys.stdin.read()
print(fun(keywords, program, C, D))

# s1 = program.strip().replace("\n", "\\\n")
# print(f">>> fun({keywords}, \"{s1}\", \"{C}\", \"{D}\")")
# print(f"'{fun(keywords, program, C, D)}'")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
