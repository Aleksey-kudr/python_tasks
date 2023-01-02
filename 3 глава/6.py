day = int(input("Day? "))
mouth = int(input("Mouth? "))
year = int(input("Year? "))

magic_number = day * mouth
if magic_number == year:
    print("magic data!!!")
else:
    print("NO magic(")