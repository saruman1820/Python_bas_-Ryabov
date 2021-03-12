# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

products, order = [], 1


def check_float(value):
    try:
        float(value)
        return float(value)
    except ValueError:
        try:
            value = value.replace(",", ".")
            return float(value)
        except ValueError:
            return False


while input("\nДобавить товар? (yes/no)").lower() in ["y", "yes", "да", "д"]:

    tmp = input('Введите название товара: ')
    while tmp == "":
        print('Наименование товара не может быть пустым!')
        tmp = input('Введите название товара: ')

    title = tmp

    tmp = input('Введите стоимость товара: ')
    while not check_float(tmp):
        print('Цена должна быть числом!')
        tmp = input('Введите стоимость товара: ')

    price = check_float(tmp)

    tmp = input('Введите количество: ')
    while not check_float(tmp):
        print('Количество должно быть числом!')
        tmp = input('Введите количество: ')

    amount = check_float(tmp)

    tmp = input('Введите единицы измерения: ')
    while tmp == "":
        print('Единица изменерения не может пустой!')
        tmp = input('Введите единицы измерения: ')

    unit = tmp

    products.append((
        order,
        {
            'title': title,
            'price': price,
            'amount': amount,
            'unit': unit
        }
    ))

    title, price, amount, unit = None, None, None, None
    order += 1

print(products)

analitics = {
    'title': [],
    'price': [],
    'amount': [],
    'unit': set()
}

for _, item in products:
    analitics['title'].append(item['title'])
    analitics['price'].append(item['price'])
    analitics['amount'].append(item['amount'])
    analitics['unit'].add(item['unit'])

print(analitics)
