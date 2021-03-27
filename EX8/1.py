"""
1. Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import datetime


class Data:
    def __init__(self, data):
        self.ins_data = str(data)

    def __str__(self):
        return self.ins_data


    @classmethod
    def extract(cls, ins_data):
        cls.valid(date_text=ins_data)
        d = int(ins_data.split("-")[0])
        m = int(ins_data.split("-")[1])
        y = int(ins_data.split("-")[2])
        return f"день={d} месяц={m}  год={y} "

    @staticmethod
    def valid(date_text):
        try:
            datetime.datetime.strptime(date_text, '%d-%m-%Y')
            return date_text
        except ValueError:
            raise ValueError("Не верный формат времени(должен быть DD-MM-YYYY) или неверная дата,")


today = Data("28-02-2021")
print(today)
print(Data.extract(today.ins_data))
print(Data.valid("27-03-2020"))

today.ins_data = "29-02-2021"
print(Data.extract(today.ins_data))


