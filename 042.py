import string


def word_value(word):
    sum = 0
    for l in word:
        sum += string.ascii_uppercase.index(l) + 1
    return sum


values_list = list()
triangle_numbers = list()

with open("p042_words.txt", "r") as f:
    words = f.readlines()[0]
    words = words.split(",")
    words = [word.replace('"', "") for word in words]

    for word in words:
        values_list.append(word_value(word))

triangle_numbers = [
    n * (n + 1) // 2
    for n in range(1, max(values_list))
    if (n * (n + 1) // 2) <= max(values_list)
]

counter = 0
for value in values_list:
    if triangle_numbers.count(value):
        counter += 1

print(counter)
