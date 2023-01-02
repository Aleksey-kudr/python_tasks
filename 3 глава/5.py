body_mass = float(input("Ваша масса: "))
ves = body_mass * 9.8

if ves > 500:
    print("Тяжелый сцука")
elif ves < 100:
    print("Легкий сцука")