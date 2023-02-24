num_packages = int(input("Введите количество пакетов: "))

total_cost = num_packages * 99

if 10 <= num_packages <= 19:
    sale = 0.1
elif 20 <= num_packages <= 49:
    sale = 0.2
elif 50 <= num_packages <= 99:
    sale = 0.3
elif num_packages >= 100:
    sale = 0.4
else:
    sale = 0.0

sale_price = total_cost * sale
total_price = total_cost - sale_price

print(f"Сумма скидки: {sale_price:.2f}")
print(f"Итоговая сумма: {total_price:.2f}")