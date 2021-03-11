second = int(input("vvedite vremya v sekundah"))
hour = second // 3600
min = ((second % 3600)//60)
sec = ((second % 3600)%60)
total="{} hours {} mins {} seconds".format(hour, min, sec)
print(total)