# ask user to input a number containing more than one digit.

"""
Insert the number : 1256
14
"""

# one = " "
# two = " "
# three = " "
# four = " "

# number = input(f"Insert the number#: 1st digit: {one} 2nd digit: {two} 3rd digit: {three} 4th digit: {four}")

# print(f"{one}+{two}+{three}+{four}")


user = input("Insert the number: ")

total = 0

i = 0
while i < len(user):  
    total = total + int(user[i])
    i = i + 1

print(total)