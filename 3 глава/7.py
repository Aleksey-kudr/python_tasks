first_color = input("First color? ")
second_color = input("Second color? ")

if first_color == "red" and second_color == "blue" or first_color == "blue" and second_color == "red":
    print("Purple!")
elif first_color == "red" and second_color == "yellow" or first_color == "yellow" and second_color =="red":
    print("Orange!")
elif first_color == "blue" and second_color == "yellow" or first_color == "yellow" and second_color == "blue":
    print("Green")
else:
    print("Error")