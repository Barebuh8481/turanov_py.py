# Функция для вычисления суммы цифр числа
def summa(num):
    return sum(int(digit) for digit in str(num))


num = int(input("Введите число: "))
steps = 0

while num != 0:
    num -= summa(num)
    steps += 1

print(f"Количество шагов до нуля: {steps}")


def prod(arr):
    product = 1
    for num in arr:
        product *= num
    return product


def average(arr):
    return sum(arr) / len(arr) if len(arr) > 0 else 0


arrays = []
for i in range(3):
    arr = list(map(int, input(f"Введите элементы массива {i+1} через пробел: ").split()))
    arrays.append(arr)

for i, arr in enumerate(arrays):
    print(f"Массив {i+1}:")
    print(f"Произведение элементов: {prod(arr)}")
    print(f"Среднее арифметическое: {average(arr):.2f}")