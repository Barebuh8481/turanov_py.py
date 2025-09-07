def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def divide(a, b, c, d):
    numerator = a * d
    denominator = b * c
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

a, b = map(int, input("Введите первую дробь (A/B): ").split('/'))
c, d = map(int, input("Введите вторую дробь (C/D): ").split('/'))

numerator, denominator = divide(a, b, c, d)
print(f"Результат деления: {numerator}/{denominator}")


def in_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 <= R**2



a, b, R = map(float, input("Введите координаты центра окружности и радиус (a b R): ").split())
points = []
for _ in range(3):
    x, y = map(float, input("Введите координаты точки: ").split())
    points.append((x, y))

count = sum(in_circle(x, y, a, b, R) for x, y in points)
print(f"Количество точек внутри окружности: {count}")


