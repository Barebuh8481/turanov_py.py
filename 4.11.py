def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


n = int(input("Введите число n (> 2): "))
twins = []

for i in range(n, 2 * n - 1):
    if is_prime(i) and is_prime(i + 2):
        twins.append((i, i + 2))

print("Пары близнецов:")
for pair in twins:
    print(pair)



def find_max(matrix):
    max_val = matrix[0][0]
    max_pos = (0, 0)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_pos = (i, j)
    return max_val, max_pos


A = [list(map(int, input("Введите строки матрицы A через пробел: ").split())) for _ in range(2)]
B = [list(map(int, input("Введите строки матрицы B через пробел: ").split())) for _ in range(2)]

max_A, pos_A = find_max(A)
max_B, pos_B = find_max(B)

A[pos_A[0]][pos_A[1]], B[pos_B[0]][pos_B[1]] = B[pos_B[0]][pos_B[1]], A[pos_A[0]][pos_A[1]]

print("Матрица A после замены:")
for row in A:
    print(row)

print("Матрица B после замены:")
for row in B:
    print(row)