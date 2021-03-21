class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'{self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки {self.title}'


brush = Stationary("кисть")
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(brush.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())
