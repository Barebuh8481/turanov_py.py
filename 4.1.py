import random

# вывод массива
def print_array(arr):
    print("Массив:", arr)

# сумма элементов массива
def sum_array(arr):
    return sum(arr)

# сред ариф значения массива
def average_array(arr):
    return sum_array(arr) / len(arr) if len(arr) > 0 else 0


array1 = [random.randint(1, 100) for _ in range(random.randint(1, 15))]
array2 = [random.randint(1, 100) for _ in range(random.randint(1, 15))]
array3 = [random.randint(1, 100) for _ in range(random.randint(1, 15))]


print_array(array1)
print(f"Сумма элементов: {sum_array(array1)}")
print(f"Среднеарифметическое: {average_array(array1):.2f}\n")


print_array(array2)
print(f"Сумма элементов: {sum_array(array2)}")
print(f"Среднеарифметическое: {average_array(array2):.2f}\n")


print_array(array3)
print(f"Сумма элементов: {sum_array(array3)}")
print(f"Среднеарифметическое: {average_array(array3):.2f}")