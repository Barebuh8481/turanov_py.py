def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def divide(a, b, c, d):
    numerator = a * d - c * b
    denominator = b * d
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor


a, b = map(int, input("Введите первую дробь (A/B): ").split('/'))
c, d = map(int, input("Введите вторую дробь (C/D): ").split('/'))

numerator, denominator = divide(a, b, c, d)
print(f"Результат вычитания: {numerator}/{denominator}")

def find_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors


n = int(input("Введите число: "))
divisors = find_divisors(n)
print("Делители:", ' '.join(map(str, divisors)))