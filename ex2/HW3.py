# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

Lseasons = ['Зима', 'Весна', 'Лето', 'Осень']
Dseasons = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
NUM_month = int(input("Введите месяц по номеру "))
if NUM_month in [1, 2, 12]:
    print(Lseasons[0])
    print(Dseasons.get(1))

elif 2 < NUM_month < 6:
    print(Lseasons[1])
    print(Dseasons.get(2))

elif 5 < NUM_month < 9:
    print(Lseasons[2])
    print(Dseasons.get(3))

elif 8 < NUM_month < 12:
    print(Lseasons[3])
    print(Dseasons.get(4))

else:
    print("Такого месяца не существует")
