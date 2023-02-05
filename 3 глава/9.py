number = int(input("Введите номер кармана: "))

if number == 0:
    print("Green")
elif 1 <= number <= 10 and (number % 2 == 0):
    print("Черный")
elif 1 <= number <= 10 and (number % 2 != 0):
    print("Красный")
elif 11 <= number <= 18 and (number % 2 != 0):
    print("Черный")
elif 11 <= number <= 18 and (number % 2 == 0):
    print("Красный")
elif 19 <= number <= 28 and (number % 2 != 0):
    print("Черный")
elif 19 <= number <= 28 and (number % 2 == 0):
    print("Красный")
elif 29 <= number <= 36 and (number % 2 != 0):
    print("Черный")
elif 29 <= number <= 36 and (number % 2 == 0):
    print("Красный")
else:
    print("Error")




