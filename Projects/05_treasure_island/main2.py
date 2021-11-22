print("Welcome to the Treasure Island.")

choice1 = input("You have come to a cross road. Where do you want to go. 'left' or 'right'? ")

if choice1 == "right":
    print("You fell into a hole. Game is over.")

elif choice1 == "left":
    choice2 = input("You have come to a lake. There is an island at the middle of the lake. Do you want to wait for a boat or swim across? ")
    
    if choice2 == "swim":
        print("You were attacked by an angry trout. Game is over.")
    
    elif choice2 == "wait":
        choice3 = input("You have arrived to an island unharmed. There is a house with 3 doors. Red Yellow and Blue. Which one would you like to choose? ")
    
        if choice3 == "red":
            print("You enter a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You find the treasure. You WIN!")
        elif choice3 == "blue":
            print("You enter a room full of beasts. Game Over")
        else:
            print("Invalid Argument.")
    
    else:
        print("Invalid Argument.")

else:
    print("Invalid Argument.")