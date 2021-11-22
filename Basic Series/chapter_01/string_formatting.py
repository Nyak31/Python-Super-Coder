first_name = "Phil"
last_name = "Contreras"
age = 33
email = "phil@contreras.com"
address = "123, Street, Korea"

# Hey! I am Phil Contreras. I am 33 years old. You can contact me on phil@contreras.com. I live in 123, Street, Korea.

print("Hey! I am Phil Contreras. I am 33 years old. You can contact me on phil@contreras.com. I live in 123, Street, Korea.")

print("Hey! I am", first_name, last_name,". I am", age, "years old. You can contact me on", email, ". I live in", address)

# Concatenation -> Joining things together
print("Hey! I am "+first_name+" "+last_name+". I am "+str(age)+" years old. You can contact me on "+email+". I live in "+address+".")

# .format method
# placeholders -> hold the place of the variables
print("Hey! I am {} {}. I am {} years old. You can contact me on {}. I live in {}.".format(first_name, last_name, age, email, address))

# f string method
print(f"Hey! I am {first_name} {last_name}. I am {age} years old. You can contact me on {email}. I live in {address}.")
