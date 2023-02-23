# Prompt user for input
num_5k = int(input("Enter the number of 5-kopeck coins: "))
num_10k = int(input("Enter the number of 10-kopeck coins: "))
num_50k = int(input("Enter the number of 50-kopeck coins: "))

# Calculate the total value of the coins entered
total_value = num_5k * 5 + num_10k * 10 + num_50k * 50

# Check if the total value equals one ruble and display the result
if total_value == 100:
    print("Congratulations, you won!")
elif total_value < 100:
    print("Sorry, the amount entered is less than one ruble.")
else:
    print("Sorry, the amount entered is more than one ruble.")
