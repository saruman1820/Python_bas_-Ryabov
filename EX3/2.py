# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя:
# имя,
# фамилия,
# год рождения,
# город проживания,
# email,
# телефон.

# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(
        fname,
        fsurname,
        fyear,
        ftown,
        femail,
        fphone):
    """
возвращяет строку с информацией по пользователе
    :param fname: имя
    :param fsurname: фамилия
    :param fyear: год рождения
    :param ftown: город проживания
    :param femail: email
    :param fphone: телефон
    :return:
    :rtype str
    """
    print(f"имя: {fname}, "
          f"фамилия: {fsurname}, "
          f"год рождения: {fyear}, "
          f"город проживания: {ftown}, "
          f"email: {femail}, "
          f"телефон: {fphone}")


name = input("Введите имя пользователя: ")
surname = input("Введите фамилю пользователя: ")
year = input("Введите год рождения пользователя: ")
town = input("Введите город проживания пользователя: ")
email = input("Введите email пользователя: ")
phone = input("Введите телефон пользователя: ")

user_info(fname=name, fsurname=surname, fphone=phone, femail=email, ftown=town, fyear=year)
