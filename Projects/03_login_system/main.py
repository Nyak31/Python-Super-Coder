### OUTPUT ::

"""
Welcome to the Login System

Insert your Username : philc
Insert your Email : phil.c@gmail.com
Insert your Password : 123456
Welcome to the System
OR
Invalid Credentials
"""

print("Welcome to the Login System")

Username = input("Insert your Username: ")
Email = input("Insert your Email: ")
Password = input("Insert your Password: ")

if Username == "phil.c" and Email == "phil.c@gmail.com" and Password == "123456":
    print("Welcome to the Login System.")
else:
    print("Invalid Credentials.")

import getpass

import sys
import msvcrt

password = ''
while True:
    x = msvcrt.getch()
    if x == '\r':
        break
    sys.stdout.write('*')
    passwor +=x

print '\n'+passwor

#pswd = getpass.getpass('Password:')