import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(f"НОД: {gcd(a, b)}")
print(f"НОК: {lcm(a, b)}")


def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def quadrat_area(a, b, c, d, diag):
    area1 = triangle_area(a, b, diag)
    area2 = triangle_area(c, d, diag)
    return area1 + area2


a, b, c, d, diag = map(float, input("Введите стороны и диагональ через пробел: ").split())
print(f"Площадь четырехугольника: {quadrat_area(a, b, c, d, diag):.2f}")