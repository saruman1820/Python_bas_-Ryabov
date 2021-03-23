"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list]))

    def __add__(self, other):
        # проверка что количество строк и скольбцов равно
        if len(self.list) == len(other.list) and len(self.list[0]) == len(other.list[0]):
            return Matrix([[self.list[j][i] + other.list[j][i] for i in range(len(self.list[0]))]
                           for j in range(len(self.list))])
        else:
            return str("Нельзя сложить матрицы с расзной шириной")


a = Matrix([[1, 2, 8],
            [1, 2, 10],
            [5, 8, 33]])

b = Matrix([[4, 8, 11],
            [4, 5, 6],
            [12, 4, 7]])

print(a + b)
