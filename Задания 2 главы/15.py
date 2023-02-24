seconds = int(input("Количество секунд: "))

if 60 <= seconds <= 3600:
    minutes = seconds // 60
    seconds = seconds % 60
    print(f"Минуты: {minutes}", f"Секунды: {seconds}")
elif seconds >= 3600:
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    print("Часы:", hours)
    print("Минуты:", minutes)
    print("Секунды:", seconds)
