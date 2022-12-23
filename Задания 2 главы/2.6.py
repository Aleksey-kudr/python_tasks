amount = float(input("Введите стоимость товара: "))
federal_nalog = amount * 0.05
region_nalog = amount * 0.025
general_nalog = federal_nalog + region_nalog
amount_with_all_nalog = amount - general_nalog
print(f"Сумма покупки: {amount}"
      f"\n Федеральный налог с продажи: {federal_nalog:.2f}"
      f"\n Региональный налог с продажи: {region_nalog:.2f}"
      f"\n Общий налог с продажи: {general_nalog:.2f}"
      f"\n Общая сумма покупки: {amount_with_all_nalog:.2f}")
