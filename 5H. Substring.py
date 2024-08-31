"""
В этой задаче Вам требуется найти максимальную по длине подстроку данной строки,
такую что каждый символ встречается в ней не более k раз.

Формат ввода
В первой строке даны два целых числа n и k (1 ≤ n ≤ 100000, 1 ≤ k ≤ n ) , где n
– количество символов в строке. Во второй строке n символов – данная строка, состоящая
только из строчных латинских букв.

Формат вывода
В выходной файл выведите два числа – длину искомой подстроки и номер её первого
символа. Если решений несколько, выведите любое.

Пример 1
Ввод
Вывод
3 1
abb

2 1

Пример 2
Ввод
Вывод
5 2
ababa

4 1
"""


class MultiSet:
    def __init__(self):
        self.d = {}

    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            return 0

    def __contains__(self, key):
        return key in self.d

    def __len__(self):
        return len(self.d)

    def __str__(self):
        return self.d.__str__()

    def add(self, key):
        if key not in self.d:
            self.d[key] = 0
        self.d[key] += 1

    def pop(self, key):
        if key in self.d:
            if self.d[key] == 1:
                self.d.pop(key)
            else:
                self.d[key] -= 1


def fun(s, k):
    """
    >>> fun("abb", 1)
    (2, 1)
    >>> fun("ababa", 2)
    (4, 1)
    >>> fun("aaaaaaaaaa", 20)
    (10, 1)
    >>> fun("aassddaassddr", 2)
    (7, 7)
    """

    def update_max(left, right, max_len, ans):
        cur_len = right - left
        if cur_len > max_len:
            max_len = cur_len
            ans = (left, right - 1)
            return ans, max_len
        else:
            return ans, max_len

    d = MultiSet()

    max_len = 0
    ans = None

    right = 0
    for left in range(len(s)):
        d.pop(s[left - 1])

        while right < len(s):
            if d[s[right]] == k:
                ans, max_len = update_max(left, right, max_len, ans)
                break
            else:
                d.add(s[right])

            right += 1
        else:
            ans, max_len = update_max(left, right, max_len, ans)
            break

    left, right = ans
    return right - left + 1, left + 1


n, k = map(int, input().split())
s = input()
print(*fun(s, k))

# print(f">>> fun(\"{s}\", {k})")
# print(f"{fun(s, k)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
