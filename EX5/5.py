# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random

file = open("5.txt", "w")
file.write(input("Введите набор чисел, разделенных пробелами: "))
file.close()


file_read = open('5.txt')
numbers = file_read.read().split()
file_read.close()
print(f"сумма чисел в файле: {sum(map(float, numbers))}")

