#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:        # Внешний цикл проходит по каждой строке матрицы
        new_row = []
        for num in row:       # Внутренний цикл проходит по каждому элементу внутри строки
            new_row.append(num ** 2)  # Квадрат каждого элемента добавляется в new_row
        new_matrix.append(new_row)    # new_row добавляется в new_matrix
    return new_matrix
