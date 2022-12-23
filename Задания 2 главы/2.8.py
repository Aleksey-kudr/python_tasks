price_food = float(input("Стоимость еды: "))
size_tips = price_food * 0.18
size_nalog = price_food * 0.07
final_price = price_food - size_nalog - size_tips
print(f"Сумма чаевых составит: {size_tips:.2f}\n"
      f"Сумма налога составит: {size_nalog:.2f}\n"
      f"Итоговая цена: {final_price:.2f}")
