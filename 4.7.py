def right_triangle_area(x, y):
    return (x * y) / 2

def pryamougilnik_area(z, t):
    return z * t


x, y, z, t = map(float, input("Введите длины сторон через пробел: ").split())
area_triangle = right_triangle_area(x, y)
area_pryamougilnik = pryamougilnik_area(z, t)
print(f"Площадь четырехугольника: {area_pryamougilnik:.2f}")
print(f"Площадь треугольника: {area_triangle:.2f}")

def to_oct(n):
    octal = oct(n)[2:].zfill(10)
    return octal

# Основная программа
n = int(input("Введите число: "))
print(f"Восьмеричный код: {to_oct(n)}")