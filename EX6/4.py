"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
speed
color
name
is_police (булево).

А также методы:
go, stop, turn(direction),

которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов:
TownCar,
SportCar,
WorkCar,
PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:

    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        """

        :param speed: скорость машины
        :param color: цвет машины
        :param name: марка/модель
        :param is_police:
        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction: str):
        if direction == "лево":
            return f"{self.name} поевернула налево"
        if direction == "право":
            return f"{self.name} поевернула направо"

    def show_speed(self):
        return f"текущая скорость машины {self.name} равна {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"текущая скорость машины {self.name} равна {self.speed}", end=" ")
        if self.speed > 60:
            return f'!!! Текущая скорость машины {self.name} явлется превышением!!!'
        else:
            return ''


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"текущая скорость машины {self.name} равна {self.speed}", end=" ")
        if self.speed > 40:
            return f'!!! Текущая скорость машины {self.name} явлется превышением!!!'
        else:
            return ''


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


audi = SportCar(100, 'зелёная', 'Audi', False)
volga = TownCar(30, 'Чёрная', 'Волга', False)
lada = WorkCar(70, 'Ржавый', 'Ваз', True)
ford = PoliceCar(110, 'Синий', 'Ford', True)

print(lada.go())
print(lada.show_speed())
print(lada.turn("лево"))
print(volga.turn("право"), audi.stop())
print(f'{lada.name}  {lada.color}')
print(audi.show_speed())
print(volga.show_speed())
