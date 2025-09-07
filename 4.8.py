def proverka(num):
    for digit in str(num):
        if digit == '0' or num % int(digit) != 0:
            return False
    return True

n = int(input("Введите число n: "))
result = [i for i in range(1, n + 1) if proverka(i)]
print("Числа, которые делятся на каждую из своих цифр:", result)


def swap(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]

m = int(input("Введите длину массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

print("Исходный массив:", arr)
swap(arr)
print("Массив после замены:", arr)