#  Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#  В расчете необходимо использовать формулу:
#  (выработка в часах*ставка в час) + премия.
#  Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def calculation(hours, pay, bonus=0):
    return check_float(hours) * check_float(pay) + check_float(bonus)


def check_float(value):
    try:
        float(value)
        return float(value)
    except ValueError:
        try:
            value = value.replace(",", ".")
            return float(value)
        except ValueError:
            return None


if len(argv) == 4:
    script_path, hours, pay, bonus = argv
    print(calculation(hours, pay, bonus))
elif len(argv) == 3:
    script_path, hours, pay = argv
    print(calculation(hours, pay))
