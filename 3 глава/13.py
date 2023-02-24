package_weight = int(input("Введите массу пакета в граммах: "))

if package_weight <= 200:
    rate = 150
elif 200 <= package_weight <= 600:
    rate = 300
elif 600 <= package_weight <= 1000:
    rate = 400
else:
    rate = 475

payment = rate * (package_weight / 100)

print(payment)