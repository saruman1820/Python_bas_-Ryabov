text = None
while text != "":
    text = input("Введите текст: ")
    file = open("1.txt", "a")
    file.write(text+"\n")
    file.close()
