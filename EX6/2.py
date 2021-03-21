'''
. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
'''


class Road:
    """
    :param length: Длина дорожного полотна в метрах
    :param width: Ширина дорожного полотна в метрах
    """
    __mass_per_sm = 0.03

    def __init__(self, length, width):

        self._length = float(length)
        self._width = float(width)

    def get_mass(self, height: float):
        return (self._length * self._width * self.__mass_per_sm * height)

    # def mass(self, _length):

try:
    new_road = Road(10, 20)
except:
    print('класс Road требует 2 позиционных аргумента')

print(new_road.get_mass(10))
