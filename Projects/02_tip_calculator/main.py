print("Welcome to the tip calculator!")



bill = int(input("What is the total bill? : "))

give = int(input("How much tip would you like to give? 10 12 or 15: "))

split = int(input("How many people to split the bill?"))

# print(Each person should pay:{bill} *1.10 or *1.12 or *1.15 / {split"})

print(f"Each person needs to pay: {(((give/100)*bill)+bill)/split}")

# BODMAS