import math


x = int(input("Введите значение x: "))
t = int(input("Введите значение t: "))


z = ((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t))))*math.pow(math.e,x)


print(f"Результат: {z:.2f}")