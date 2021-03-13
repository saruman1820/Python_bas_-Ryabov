# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
def power(a, n):
    """

    :param a:
    :param n:
    :return:
    """
    if a == 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return a
    elif n < 0:
        return 1 / (a * power(a, -n - 1))
    else:
        return a * power(a, n - 1)


x = int(input("Введите действительное положительное число: "))
while True:
    if x < 0:
        x = int(input("число должно быть действительное положительное: "))
        continue
    break

y = int(input("Введите целое отрицательное число: "))
while True:
    if y >= 0:
        y = int(input("число должно быть целым отрицательным: "))
        continue
    break

print(f"без использования ** {power(a=x, n=y)}")
print(f"c использованием  ** {power(a=x, n=y)}")


def power2(a, n):
    n = abs(n)
    return 1 / a ** n
