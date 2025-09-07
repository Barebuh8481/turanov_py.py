a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

result = []

if 1 <= a <= 3:
    result.append(a)

if 1 <= b <= 3:
    result.append(b)

if 1 <= c <= 3:
    result.append(c)


if result:
    print("Числа, принадлежащие интервалу [1, 3]:", result)
else:
    print("Нет чисел, принадлежащих интервалу [1, 3].")