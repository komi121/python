"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса 
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы 
складываем с первым элементом первой строки второй матрицы и т.д.
"""

def make_matrix(line,colunm):
    matrix = []
    for i in range(colunm):
        temp =[]
        for j in range(line):
            temp.append(0)
        matrix.append(temp)
    return matrix 


class Matrix:
    def __init__(self, list_lists:list):
        self.matrix = list_lists
        self.line = len(list_lists[0])
        self.column = len(list_lists)
    def __str__(self):
        matrix_str = ''
        for i in range (self.column):
            for j in range (self.line):
                matrix_str += str(self.matrix[i][j])
                matrix_str += "\t"
            matrix_str += '\n'
        return matrix_str
    def __add__(self,other):
        self.matrix_sum = make_matrix(self.line, self.column)
        for i in range (self.column):
            for j in range (self.line):
                self.matrix_sum[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return self.matrix_sum


list_list = [[-31,2,1],
             [1,2,1],
             [1,2,1]
]
list_list1 = [[87,1,10],
             [0,10,0],
             [10,1,0]
]




mat = Matrix(list_list)
mat2 = Matrix(list_list1)
mat_sum = mat + mat2
print(mat)
print(mat_sum)


