# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


try:
    f_obj = open("1.txt", "r")
    content = f_obj.readlines()
    print(content)
    lines = len(content)
    for index, el in enumerate(content, 1):
        print(f"В {index}-й строке {len(el.split())} слов(a)")
    print(f"в файле {lines} строк(и)")



except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f_obj.close()
