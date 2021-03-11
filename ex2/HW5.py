# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]

while True:
    new_value = input("\nнажмите ENTER без значения для выхода \n"
                      "Ведите новое значение: ")
    new_value = new_value.replace(" ", "")
    if new_value.isdigit():
        new_value = int(new_value)
        temp_value = new_value
        # Поиск индекса
        while True:
            if (temp_value - 1) in my_list:
                new_value_index = my_list.index(temp_value)
                break
            else:
                temp_value -= 1

        my_list.insert(new_value_index + 1, new_value)
        print(type(new_value))
        print(new_value)
        print(f"Сейчас следубщие занчения {my_list}")
    elif new_value == "":
        break
    else:
        print(f"вы ввели {new_value} а надо положительное целое число")
