'''
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
'''

import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof += profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'avg_profit': round(prof_aver)}

    print(f'Прибыль каждой компании - {profit}')
    print(f'средняя перибыль - {pr}')
    list = [profit, pr]

with open('7.json', 'w') as write_js:
    json.dump(list, write_js)
    # json.dump(, write_js)
with open('7.json', "r") as write_js:
    js_str = write_js.readline()
print(f'Создан файл с расширением json со следующим содержимым: \n '
      f' {(js_str)}')
