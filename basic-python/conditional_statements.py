temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# if and (&&) or (||)

# Chaining Comparison Operators
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")
