"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
    для пальто (V/6.5 + 0.5),
    для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.

"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.area + other.area

    @property
    @abstractmethod
    def area(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def area(self):
        return self.size / 6 + 0.5


class Costume(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def area(self):
        return self.height * 2 + 0.5


a = Coat("пальто 1", 12)
b = Costume("Костюм 1", 2)

print(a.area)
print(b.area)
print(a + b)
