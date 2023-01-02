speed = int(input("Ваша скорость: "))

if 0 <= speed <= 200:
    print("Okey!")
elif speed < 0 or speed > 200:
    print("Noooo!")