for number in range(3):
    print("Attempt", number)
# Attempt 0
# Attempt 1
# Attempt 2

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
# Attempt 1 .
# Attempt 2 ..
# Attempt 3 ...

for number in range(1, 4):
    print("Attempt", number)
# Attempt 0
# Attempt 1
# Attempt 2

for number in range(1, 10, 2):
    print("Attempt", number)
# Attempt 1
# Attempt 3
# Attempt 5
# Attempt 7
# Attempt 9

# Jump out of loop
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# Nested loop

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
