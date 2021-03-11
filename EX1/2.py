time_user_input = int(input("вводите время в секундах >>> "))
hours = time_user_input // 3600
if hours < 10:
    hours = "0" + str(hours)
minutes = (time_user_input // 60) % 60
if minutes < 10:
    minutes = "0" + str(minutes)
seconds = time_user_input % 60
if seconds < 10:
    seconds = "0" + str(seconds)
print(f"При переводе в формат чч:мм:сс получаем: {hours}:{minutes}:{seconds}")
