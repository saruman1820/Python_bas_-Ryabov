# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу
def f_input():
    user_input = (input("\t\t\t\t\t!!!Для выхода введите q!!!\n"
                        "\t\t\t\t\t!!!Все числа после q будут откинуты!!!\n"
                        "Введите числа через пробел, которые необходимо просуммировать: ")).split()

    if "q" in user_input:
        user_input = user_input[:user_input.index("q")]
        return user_input, False
    return user_input, True

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

summa = 0
con_loop = True
while con_loop:
    print(f"\t\t\t\t\tПромежуточная сумма равна {summa}")
    a = f_input()
    con_loop = a[1]
    for i in a[0]:
        summa = summa + check_float(i)

print(summa)
