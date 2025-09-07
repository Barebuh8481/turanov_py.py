import math


def hypotenusa(a, b):
    return math.sqrt(a**2 + b**2)

a1, b1 = map(float, input("Введите катеты 1 треугольника через пробел: ").split())
a2, b2 = map(float, input("Введите катеты 2 треугольника через пробел: ").split())

h1 = hypotenusa(a1, b1)
h2 = hypotenusa(a2, b2)

if h1 > h2:
    print(f"Гипотенуза 1 треугольника ({h1:.2f}) больше.")
elif h1 < h2:
    print(f"Гипотенуза 2 треугольника ({h2:.2f}) больше.")
else:
    print("Гипотенузы равны.")

def word_sorting(word):
    return ''.join(sorted(word))

def sort_string(string):
    words = string.split()
    return ' '.join(word_sorting(word) for word in words)

string = input("Введите строку: ")
print(f"Отсортированная строка: {sort_string(string)}")