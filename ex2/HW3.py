# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

lseasons = ['Зима', 'Весна', 'Лето', 'Осень']
Dseasons = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
NUM_month = int(input("Введите месяц по номеру "))
# Реализация через список
if NUM_month in [1, 2, 12]:
    print(lseasons[0])
elif 2 < NUM_month < 6:
    print(lseasons[1])
elif 5 < NUM_month < 9:
    print(lseasons[2])
elif 8 < NUM_month < 12:
    print(lseasons[3])
else:
    print("Такого месяца не существует")

# Реализация через словарь
dseasons = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
for k, v in dseasons.items():
    if NUM_month in v:
        print(k)
