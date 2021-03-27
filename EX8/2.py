"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""

class MyZeroDivision(Exception):
    text = "Деление на ноль запрещено"

    def __str__(self):
        return self.text


class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise MyZeroDivision

        return Number(float(self) / float(other))



try:
    dividend, divider = map(Number, input("Введите делимое и делитель через пробел: ").split())
    print(dividend / divider)
except MyZeroDivision as e:
    print(e)
except ValueError as e:
    print(e)

