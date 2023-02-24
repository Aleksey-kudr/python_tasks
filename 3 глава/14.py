growth = float(input("Введите ваш рост в метрах: "))
weight = int(input("Введите ваш вес в кг: "))

IMT = weight / growth ** 2

if IMT < 18.5:
    print("Ниже нормы")
elif IMT > 25:
    print("Больше нормы")
else:
    print("НОРМ")

print(f"Ваш ИМТ {IMT:.2f}")