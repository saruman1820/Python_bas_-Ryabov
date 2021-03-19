# Создать (не программно) текстовый файл со следующим содержимым:
# One - 1
# Two - 2
# Three - 3
# Four - 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

SRC_FILENAME = "4.txt"
DST_FILENAME = "4_dst.txt"

NUMERALS = {"One": 'Один', "Two": 'Два', "Three": 'Три', "Four": 'Четыре'}
# print(NUMERALS.get("One"))

with open(SRC_FILENAME) as f_obj:
    lines = f_obj.readlines()
for el in lines:
    chis, numb = el.replace("\n", '').split()
    chis = NUMERALS.get(chis)

