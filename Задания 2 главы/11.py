man = int(input("Сколько мужиков в классе? "))
woman = int(input("Сколько девушек в классе? "))
print(f"Процент мужиков равен: {man / (man + woman)}\n"
      f"Процент девушек равен: {woman / (man + woman)}")