#geraldworks

print("\nWelcome to Python Pizza Deliveries!\n")
print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25\n")
print("Pepperoni for Small Pizza: + $2")
print("Pepperoni for Medium or Large pizza: + $3\n")
print("Extra cheese for any size pizza: + $1\n")

size = input("What size pizza do you want? S, M, L -> ")
add_pepperoni = input("Do you want pepperoni? Y or N -> ")
extra_cheese = input("Do you want extra cheese? Y or N -> ")

bill = 0

if size == 'S' or size == 's':
    bill += 15
elif size == 'M' or size == 'm':
    bill += 20
else:
    bill += 25




print(f"Your final bill is: ${bill}")
