# import re


def find_all_substrings(string, substring):
    # Initialize an empty list to store the
    # indices of all occurrences of the substring.
    indices = []
    # Set the starting index i to 0.
    i = 0
    # Use a while loop to keep searching for
    # the substring in the string.
    while i < len(string):
        # Use the find() method to find the first
        # occurrence of the substring in the string
        j = string.find(substring, i)
        # If find() returns -1, it means that there
        # are no more occurrences of the substring in
        # the string, so break out of the loop.
        if j == -1:
            break
        indices.append(j)
        i = j + len(substring)
    # Return the list of indices.
    return indices


f = open("input.txt", "r")
text = f.read().strip()

text_new = text.replace("\n\n", "\n")
while text_new != text:
    text = text_new
    text_new = text_new.replace("\n\n", "\n")


s = "Формат ввода", "Формат вывода", "Пример", "Примечания", "Результат работы"

for i in s:
    if text.find(i) != -1:
        # idx = [m.start() for m in re.finditer(i, text)]
        idx = find_all_substrings(text, i)

        for x in idx[::-1]:  # если вставлять сначала, то индексы мест вставки меняются
            text = text[:x] + "\n" + text[x:]

ans = ""
for string in text.split("\n"):
    string = string.strip()  # чтобы табуляцию заменить на \n
    if len(string) < 80:
        ans += string + "\n"
    else:
        words = string.split(" ")
        string_new = ""
        for word in words:
            if len(string_new) < 80:
                string_new += word + " "
            else:
                ans += string_new + "\n"
                string_new = word + " "

        ans += string_new + "\n"

f = open("output.txt", "w")
f.write('"""\n' + ans + '"""\n\n\n')

template = """
def fun(s):
    \"\"\"
    >>> fun([0, 1, 10, 9])
    ([0, 1], [9, 10], [3])
    >>> fun([1, 2])
    ([2], [1], [3])
    >>> fun([])
    ([], [], [])
    \"\"\"

    return


N, M = map(int, input().split())
s = [int(input()) for _ in range(N)]
print(*fun(s))

# print(f">>> fun({s})")
# print(f"{fun(s)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
"""

f.write(template)
