# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

vv_stroka = input("Введите строку: ")
sp_stroka = vv_stroka.split(" ")

# удаляем несколько пробелов подряд и пустые слова
while True:
    try:
        sp_stroka.pop(sp_stroka.index(""))
    except ValueError:
        break

# печать с проверкой условия 10 букв в слове
for i in range(0, len(sp_stroka)):
    if len(sp_stroka[i]) > 10:
        print(f"{i + 1}) {sp_stroka[i][0:10]}")
    elif len(sp_stroka[i]) <= 10:
        print(f"{i + 1}) {sp_stroka[i]}")
print(sp_stroka)
