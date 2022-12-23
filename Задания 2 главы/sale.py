original_price = float(input("Введите исходную цену: "))
discount = float(input("Введите процент скидки: ")) / 100
discount_s = original_price * discount
finish_price = original_price - discount_s
print("Цена со скидкой: ", finish_price)
