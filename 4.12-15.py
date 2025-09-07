import math

#суммы делителей числа
def sum_of_divisors(num):
    return sum(i for i in range(1, num) if num % i == 0)


N = int(input("Введите число N: "))
pairs = []

for a in range(1, N + 1):
    b = sum_of_divisors(a)
    if b > a and sum_of_divisors(b) == a:
        pairs.append((a, b))

print("Пары дружественных чисел:")
for pair in pairs:
    print(pair)


#медианы треугольника

def mediana(a, b, c):
    return 0.5 * math.sqrt(2 * (b**2 + c**2) - a**2)

a, b, c = map(float, input("Введите стороны треугольника через пробел: ").split())

m1 = mediana(a, b, c)
m2 = mediana(b, a, c)
m3 = mediana(c, a, b)

print(f"Медианы треугольника: {m1:.2f}, {m2:.2f}, {m3:.2f}")

# является ли число числом Армстронга
def is_armstrong(num):
    digits = list(map(int, str(num)))
    n = len(digits)
    return num == sum(digit**n for digit in digits)

k = int(input("Введите число k: "))
armstrong_numbers = [i for i in range(1, k + 1) if is_armstrong(i)]

print("Числа Армстронга:")
print(armstrong_numbers)


# угл между осью абсцисс и лучом
def angle_with_x_axis(x, y):
    return math.atan2(y, x)

points = []
for _ in range(3):
    x, y = map(float, input("Введите координаты точки через пробел: ").split())
    points.append((x, y))

min_angle = float('inf')
closest_point = None

for point in points:
    angle = angle_with_x_axis(*point)
    if angle < min_angle:
        min_angle = angle
        closest_point = point

print(f"Ближайшая к оси абсцисс точка: {closest_point}")

#кол-во делителей числа
def count_divisors(num):
    return sum(1 for i in range(1, num + 1) if num % i == 0)

M, N = map(int, input("Введите границы интервала M и N через пробел: ").split())
max_divisors = 0
result = []

for num in range(M, N + 1):
    div_count = count_divisors(num)
    if div_count > max_divisors:
        max_divisors = div_count
        result = [num]
    elif div_count == max_divisors:
        result.append(num)

print("Числа с наибольшим количеством делителей:")
print(result)