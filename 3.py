
kg1 = float(input("Введите цену 1 кг конфет: "))


print("Стоимость конфет:")
for kg in range(1, 11):
    cost = kg1 * kg
    print(f"{kg} кг конфет стоит {cost:.2f} рублей")