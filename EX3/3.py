# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    list = [num1, num2, num3]
    list.remove(min(list))
    return list[0] + list[1]


print(my_func(1, 11, 100))
