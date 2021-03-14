"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
"""
from itertools import cycle
from itertools import count


def a():
    first_number = int(input("введите первое число: "))
    end_number = int(input("введите конечное число число: "))
    c = 0
    for el in count(first_number):
        if c >= end_number:
            break
        print(el)
        c += 1


def b():
    first_str = list(input("введите список: ").split())
    end_str = int(input("введите число повторений списка: "))
    c = len(first_str) * end_str
    for el in cycle(first_str):
        if c <= 0:
            break
        print(el)
        c -= 1


#a()
b()
