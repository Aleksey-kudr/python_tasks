age = float(input("Введите ваш возраст: "))

if age <= 1:
    print("Младенец")
elif 1 < age < 13:
    print("Kid")
elif 13 <= age <= 20:
    print("Podrostok")
else:
    print("Взрослый")