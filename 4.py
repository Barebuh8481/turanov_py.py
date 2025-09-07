import math

# круг
def area_circle(radius):
    return math.pi * radius**2

# прямоугольник
def area_rectangle(length, width):
    return length * width

# формула Герона
def area_triangle(a, b, c):
    # полупериметр
    p = (a + b + c) / 2
    # площадь по формуле Герона
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


print("Выберите фигуру для вычисления площади:")
print("1. Круг")
print("2. Прямоугольник")
print("3. Треугольник")

choice = int(input("Введите номер фигуры: "))

if choice == 1:
    radius = float(input("Введите радиус круга: "))
    print(f"Площадь круга: {area_circle(radius):.2f}")
elif choice == 2:
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    print(f"Площадь прямоугольника: {area_rectangle(length, width):.2f}")
elif choice == 3:
    a = float(input("Введите первую сторону треугольника: "))
    b = float(input("Введите вторую сторону треугольника: "))
    c = float(input("Введите третью сторону треугольника: "))
    if a + b > c and a + c > b and b + c > a:  # Моежт ли быть треугольник
        print(f"Площадь треугольника: {area_triangle(a, b, c):.2f}")
    else:
        print("Треугольник с такими сторонами не существует")
else:
    print("Неверный выбор")