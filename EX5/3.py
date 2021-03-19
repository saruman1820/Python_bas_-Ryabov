# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

list = []
sum = 0
my_f = open('3.txt', encoding='utf-8')
content = my_f.readlines()

my_f.close()
for el in content:
    lname, salary = el.replace("\n", '').split()
    sum += float(salary)
    if float(salary) < 20000:
        list.append(lname)
print(f'Средняя величина дохода сотрудников: {round(sum / len(content), 2)}')
print(f"Cотрудники имющие оклад менее 20 тыс.{list}")
