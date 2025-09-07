import math


def triangle_area(a):
    return (math.sqrt(3) / 4) * a**2

def hexagon_area(a):
    return 6 * triangle_area(a)

a = float(input("Введите сторону шестиугольника: "))
print(f"Площадь правильного шестиугольника: {hexagon_area(a):.2f}")

def area(a, b):
    return a * b

for i in range(3):
    a = float(input(f"Введите одну сторону прямоугольника {i+1}: "))
    b = float(input(f"Введите вторую сторону прямоугольника {i+1}: "))
    print(f"Площадь прямоугольника {i+1}: {area(a, b)}")