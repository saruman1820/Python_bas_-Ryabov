# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

input_number = input("Ведите целое положительное число: ")

i = 0
result = 0
while i < len(input_number):
    if result < int(input_number[i]):
        result = int(input_number[i])
    i += 1
print("самя большая цифра в числе:", result)
