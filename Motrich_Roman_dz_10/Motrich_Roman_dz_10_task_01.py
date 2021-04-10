'''
1. Реализовать класс Matrix (матрица).
Конструктор класса __init__() должен принимать
список списков чисел для задания превоначального состояния матрицы.
Подсказка: матрица — это таблица размером N строк на M столбцов (размерность N x M).
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
В методе __init__() надо проверить корректность передаваемых
данных - все списки должны быть одинаковой длины.
В случае расхождения выбрасывать исключение ValueError с
соответствующим описанием.
Добавить метод __add__() сложения двух матриц. Складывать
можно матрицы одинаковой размерности.
В случае, когда пользователь пытается сложить матрицы разных
размеров выбросить исключение ValueError.
В результате сложения двух матриц должна образоваться новая
матрица размером N x M, где каждый элемент в ячейке i,j образован
сложением значений из соответствующих ячеек исходных матриц.
Реализовть метод __str__(), возвращающий строку вида " 1 2 3\n 4 5 6",
отводя под числа по три разряда, чтобы для небольших чисел матрица выглядела как таблица.
Создать три матрицы (две одинаковые по размеру и одну с другим размером).
Сложить одинаковые матрицы и потом сложить разные. Напечатать исходные таблицы и результат сложения.

'''


class Matrix:
    def __init__(self, input_matrix):
        if type(input_matrix)==list:
            self.matrix_h=len(input_matrix)
            self.matrix_w=len(input_matrix[0])
            elem_type=type(input_matrix[0][0])

            for string_m in input_matrix:

                if len(string_m)!= self.matrix_w:
                    raise ValueError('нашлась неправильная строка')
                else:

                    for i in string_m:
                        if type(i)!= int:
                            raise ValueError('Нашёлся неверный тип')
                        else:
                            pass
        else:
            raise ValueError('NOT LIST - very bad')
        self.matrix=input_matrix

    def __add__(self, other):

        sum_matrix = []

        if self.matrix_w!= other.matrix_w or self.matrix_h!= other.matrix_h:
            raise ValueError("Несоответствующая размерность")#else ''

        for i in range(self.matrix_h):
            tmp_list=[]
            for k in range(self.matrix_w):
                tmp_list.append(self.matrix[i][k]+self.matrix[i][k])
            sum_matrix.append(tmp_list)

        return Matrix(sum_matrix)

    def __str__(self):
        ret_srt=[]
        for i in range(self.matrix_h):
            for k in range(self.matrix_w):
                ret_srt.append('{0:^3}'.format(self.matrix[i][k]))
            ret_srt.append('\n')
        return ' '.join(ret_srt)








m=Matrix([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
n=Matrix([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
n2=Matrix([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[4,5,6]])
print(m)
print(n)
c=m+n
print(c)
print('-----------')
print(m)
print(n2)
c=m+n2
print(c)