"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class MyComplex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма c1 и c2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение c1 и c2 равно')
        return f'z = {self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c1 = MyComplex(2, 1)
c2 = MyComplex(3, 4)
print(c1)
print(c2)
print(c1 + c2)
print(c1 * c2)
