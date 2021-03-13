# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def dev_0(num1, num2):
    try:
        result = (num1 / num2)
        return result
    except ZeroDivisionError:
        return print("Нельзя делить на 0")


while True:
    a = float(input("Введите  делимое"))
    b = float(input("деление делитель"))
    print(dev_0(a, b))
