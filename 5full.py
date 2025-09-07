import random

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def generate_matrix(rows, cols, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def diagonal_sum(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))




def variant_1():
    N = int(input("Введите размер матрицы N: "))
    matrix = generate_matrix(N, N)
    print("Исходная матрица:")
    print_matrix(matrix)

    vsego_sum = 0
    count_positive = 0
    for i in range(N):
        for j in range(i + 1, N):
            if matrix[i][j] > 0:
                vsego_sum += matrix[i][j]
                count_positive += 1

    print(f"Сумма положительных элементов над главной диагональю: {vsego_sum}")
    print(f"Количество положительных элементов над главной диагональю: {count_positive}")

def variant_2():
    N = int(input("Введите размер квадратной матрицы N: "))
    matrix = generate_matrix(N, N)
    print("Исходная матрица:")
    print_matrix(matrix)

    target_sum = sum(matrix[0])
    is_true = True

    for row in matrix:
        if sum(row) != target_sum:
            is_true = False

    transposed = transpose_matrix(matrix)
    for col in transposed:
        if sum(col) != target_sum:
            is_true = False

    if is_true:
        print("Матрица является магическим квадратом.")
    else:
        print("Матрица не является магическим квадратом.")

def variant_3():
    N = int(input("Введите размер квадратной матрицы N: "))
    matrix = generate_matrix(N, N)
    print("Исходная матрица:")
    print_matrix(matrix)

    symmetrichno = True
    for i in range(N):
        for j in range(i + 1, N):
            if matrix[i][j] != matrix[j][i]:
                symmetrichno = False

    if symmetrichno:
        print("Матрица симметрична относительно главной диагонали.")
    else:
        print("Матрица не симметрична относительно главной диагонали.")

def variant_4():
    N = int(input("Введите количество строк N: "))
    M = int(input("Введите количество столбцов M: "))
    matrix = generate_matrix(N, M)
    print("Исходная матрица:")
    print_matrix(matrix)

    max_sum = float('-inf')
    min_sum = float('inf')
    max_row = []
    min_row = []

    for row in matrix:
        current_sum = sum(row)
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row
        if current_sum < min_sum:
            min_sum = current_sum
            min_row = row

    print(f"Строка с наибольшей суммой ({max_sum}): {max_row}")
    print(f"Строка с наименьшей суммой ({min_sum}): {min_row}")

def variant_5():
    N = int(input("Введите количество строк N: "))
    M = int(input("Введите количество столбцов M: "))
    matrix = generate_matrix(N, M)
    print("Исходная матрица:")
    print_matrix(matrix)

    for i in range(N):
        matrix[i].sort()

    print("Матрица после сортировки строк:")
    print_matrix(matrix)

def variant_6():
    N = int(input("Введите размер квадратной матрицы N: "))
    matrix = generate_matrix(N, N)
    print("Исходная матрица:")
    print_matrix(matrix)

    max_in_rows = [max(row) for row in matrix]
    min_in_cols = [min(col) for col in transpose_matrix(matrix)]

    print("Наибольший элемент в каждой строке:")
    print(max_in_rows)
    print("Наименьший элемент в каждом столбце:")
    print(min_in_cols)

def variant_7():
    N = int(input("Введите размер квадратной матрицы N: "))
    matrix = generate_matrix(N, N)
    print("Исходная матрица:")
    print_matrix(matrix)

    sym_matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            sym_matrix[i][j] = sym_matrix[j][i] = matrix[i][j - i]

    print("Симметричная матрица:")
    print_matrix(sym_matrix)

def variant_8():
    N = int(input("Введите размер квадратной матрицы N: "))
    k = int(input("Введите номер строки для деления: ")) - 1
    matrix = generate_matrix(N, N)
    print("Исходная матрица:")
    print_matrix(matrix)

    if matrix[k][k] != 0:
        matrix[k] = [element / matrix[k][k] for element in matrix[k]]
    else:
        print("На ноль делит ьнельзя")

    print("Матрица после деления:")
    print_matrix(matrix)

def variant_9():
    N = int(input("Введите размер квадратной матрицы N: "))
    k = int(input("Введите число k: "))
    matrix = generate_matrix(N, N)
    print("Исходная матрица:")
    print_matrix(matrix)



    count_k = 0
    max_k = float('-inf')

    for row in matrix:
        for element in row:
            if element % k == 0:
                count_k += 1
                if element > max_k:
                    max_k = element

    print(f"Число элементов, кратных {k}: {count_k}")
    print(f"Наибольший элемент, кратный {k}: {max_k}")

def variant_10():
    N = int(input("Введите количество строк N: "))
    M = int(input("Введите количество столбцов M: "))
    matrix = generate_matrix(N, M)
    print("Исходная матрица:")
    print_matrix(matrix)

    sorted_rows = []
    for row in matrix:
        if row == sorted(row) or row == sorted(row, reverse=True):
            sorted_rows.append(row)

    if sorted_rows:
        max_element = max(max(row) for row in sorted_rows)
        print(f"Максимальный элемент среди упорядоченных строк: {max_element}")
    else:
        print("Нет упорядоченных строк.")

def variant_11():
    N = int(input("Введите размер квадратной матрицы N: "))
    matrix = generate_matrix(N, N)
    print("Исходная матрица:")
    print_matrix(matrix)



# min_row_index = next(i for i, row in enumerate(matrix) if min(row) == min_element) можно было бы
    min_element = min(min(row) for row in matrix)
    min_row_index = None
    for i, row in enumerate(matrix):
        if min(row) == min_element:
            min_row_index = i
            break
    min_row_sum = sum(matrix[min_row_index])

    print(f"Сумма элементов строки, содержащей минимальный элемент: {min_row_sum}")

def variant_12():
    N = int(input("Введите размер квадратной матрицы N: "))
    matrix = generate_matrix(N, N)
    print("Исходная матрица:")
    print_matrix(matrix)

    matching_rows = []
    for i in range(N):
        if matrix[i] == list(transpose_matrix(matrix)[i]):
            matching_rows.append(i + 1)

    print(f"Строки, совпадающие со своими столбцами: {matching_rows}")

def variant_13():
    N = int(input("Введите количество строк N: "))
    M = int(input("Введите количество столбцов M: "))
    matrix = generate_matrix(N, M)
    print("Исходная матрица:")
    print_matrix(matrix)

    min_even_rows = []
    for i in range(1, N, 2):
        min_even_rows.append(min(matrix[i]))

    print("Наименьший элемент каждой четной строки:")
    print(min_even_rows)

def variant_14():
    N = int(input("Введите размер квадратной матрицы N: "))
    m = int(input("Введите номер строки для перестановки (m): "))
    matrix = generate_matrix(N, N)
    print("Исходная матрица:")
    print_matrix(matrix)

    max_diag = max((matrix[i][i], i) for i in range(N))
    matrix[max_diag[1]], matrix[m - 1] = matrix[m - 1], matrix[max_diag[1]]

    print("Матрица после перестановки:")
    print_matrix(matrix)

def variant_15():
    N = int(input("Введите количество строк N: "))
    M = int(input("Введите количество столбцов M: "))
    c = int(input("Введите значение c: "))
    d = int(input("Введите значение d: "))
    matrix = generate_matrix(N, M)
    print("Исходная матрица:")
    print_matrix(matrix)

    for i in range(N):
        if c in matrix[i]:
            matrix[i] = [element * d for element in matrix[i]]

    print("Матрица после умножения:")
    print_matrix(matrix)







def main():
    print("Практическая работа 5. Работа с двумерными массивами.")
    while True:
        print("Выберите номер варианта (1-15) или введите 0, чтобы выйти:")
        choice = input("Ваш выбор: ")

        if choice == '0':
            print("Программа завершена.")
            break

        try:
            choice = int(choice)
            if choice == 1:
                variant_1()
            elif choice == 2:
                variant_2()
            elif choice == 3:
                variant_3()
            elif choice == 4:
                variant_4()
            elif choice == 5:
                variant_5()
            elif choice == 6:
                variant_6()
            elif choice == 7:
                variant_7()
            elif choice == 8:
                variant_8()
            elif choice == 9:
                variant_9()
            elif choice == 10:
                variant_10()
            elif choice == 11:
                variant_11()
            elif choice == 12:
                variant_12()
            elif choice == 13:
                variant_13()
            elif choice == 14:
                variant_14()
            elif choice == 15:
                variant_15()
            else:
                print("Неверный выбор варианта. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите число от 0 до 15.")

if __name__ == "__main__":
    main()