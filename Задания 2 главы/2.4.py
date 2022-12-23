item_1 = float(input("Цена товара 1: "))
item_2 = float(input("Цена товара 2: "))
item_3 = float(input("Цена товара 3: "))
item_4 = float(input("Цена товара 4: "))
item_5 = float(input("Цена товара 5: "))

summary_no_nalog = item_1 + item_2 + item_3 + item_4 + item_5
nalog = summary_no_nalog * 0.07
summary_with_nalog = summary_no_nalog - nalog
print(f"Итоговая сумма без налога: {summary_no_nalog}")
print(f"Налог составит: {nalog}")
print(f"Итоговая сумма с налогом равна: {summary_with_nalog}")