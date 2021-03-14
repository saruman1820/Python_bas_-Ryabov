# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

from itertools import count


def fact(end_number):
    result = 1
    for el in count(1):
        if el > end_number:
            break
        result *= el
        yield result


end_number = int(input("введите конечное число число: "))

print(f"первые n чисел, начиная с 1! и до {end_number}! {[el for el in fact(end_number)]}") 
