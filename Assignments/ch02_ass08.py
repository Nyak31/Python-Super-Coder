# Sum of the n natural numbers
# ask a user for natural number (n)
# print total from 1 to n

user_input = int(input("Welcome, pick a number: "))

total = 0

x = 1

while x <= user_input:
    total = total + x
    x = x + 1

print(total)

