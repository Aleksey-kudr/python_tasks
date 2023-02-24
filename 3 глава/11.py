amount_books = int(input("Введите количество книг в месяц: "))

if amount_books == 0:
    point = 0
elif amount_books == 2:
    point = 4
elif amount_books == 4:
    point = 15
elif amount_books == 6:
    point = 30
elif amount_books >= 8:
    point = 60

print(point)