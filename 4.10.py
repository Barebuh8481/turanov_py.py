def check(num, digits):
    return all(digit in digits for digit in str(num))




N = int(input("Введите верхнюю границу N: "))
a, b, c = map(str, input("Введите цифры a, b, c через пробел: ").split())
digits = {a, b, c}

count = 0
for num in range(100, N + 1):
    if check(num, digits):
        count += 1

print(f"Количество чисел, составленных из цифр {a}, {b}, {c}: {count}")


def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

sentence = input("Введите строку: ")
print(f"Обратная последовательность слов: {reverse_words(sentence)}")