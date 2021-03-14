# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка
from functools import reduce

my_list = [el for el in range(100, 1001, 2)]
print(my_list)
print(reduce(lambda prev_el, el: prev_el * el, my_list,1))
