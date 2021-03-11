#  Для списка реализовать обмен значений соседних элементов, т.е.
#  Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#  При нечетном количестве элементов последний сохранить на своем месте.
#  Для заполнения списка элементов необходимо использовать функцию input().


list = []
n = int(input("Введите количество элемнтов списка:"))
'''
while True:
    list_stop_ans = ["n", "no", "нет", "н"]
    stop_ans = input("введи свой ответ:")
    print(bool(list_stop_ans.count(stop_ans.lower())))
'''

for i in range(0, n):
    ele = int(input(f"введите {i + 1} элемент массива: "))
    list.append(ele)  # adding the element

if (n % 2) > 0:
    n -= 1

i = 0
while i < n - 1:
    temp_element = list[i]
    list[i] = list[i + 1]
    list[i + 1] = temp_element
    i += 2
print(list)
