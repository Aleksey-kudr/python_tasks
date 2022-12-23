length_ridge = int(input("Длина гряды в метрах: "))
area = int(input("Пространство, занимаемое концевой опорой в метрах: "))
range_grape = int(input("Расстояние между виноградными лозами: "))
amount_grape = (length_ridge - 2 * area) / range_grape
print(f"Количество виноградных лоз на гряде: {amount_grape}")