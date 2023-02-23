# Prompt user for input
num_participants = int(input("Enter the number of picnic participants: "))
num_hotdogs_per_person = int(input("Enter the number of hot dogs per participant: "))

# Calculate the minimum number of sausage packs and bun packs needed
num_hotdogs_needed = num_participants * num_hotdogs_per_person
num_sausage_packs_needed = (num_hotdogs_needed + 9) // 10
num_bun_packs_needed = (num_hotdogs_needed + 7) // 8

# Calculate the number of sausages and buns left over
num_sausages_leftover = (num_sausage_packs_needed * 10) - num_hotdogs_needed
num_buns_leftover = (num_bun_packs_needed * 8) - num_hotdogs_needed

# Display the results
print("Minimum number of sausage packs needed: ", num_sausage_packs_needed)
print("Minimum number of bun packs needed: ", num_bun_packs_needed)
print("Number of sausages left over: ", num_sausages_leftover)
print("Number of buns left over: ", num_buns_leftover)
