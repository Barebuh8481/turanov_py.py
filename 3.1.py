
sumofnumbers = 0
countofnumbers = 0


number = int(input("Введите число (окончание ввода -- 0): "))
while number != 0:
    sumofnumbers += number
    countofnumbers += 1
    number = int(input("Введите число (окончание ввода -- 0): "))


if countofnumbers > 0:
    print(f"Сумма всех чисел: {sumofnumbers}")
    print(f"Количество чисел: {countofnumbers}")
else:
    print("вы не ввели ни одного числа")