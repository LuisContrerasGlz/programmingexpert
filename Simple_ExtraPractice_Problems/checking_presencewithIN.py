# Checking the presence of something with the IN keyword

invited_guests = ["Luis", "Fernando", "Abril", "Barbara"]
name = input("Whats your name? ")

if name in invited_guests:
    print("Welcome")
else:
    print("You are not in the list, sorry ")

# Using not in now

if name not in invited_guests:
    print("You are not in the list, sorry ")
else:
    print("Welcome")
