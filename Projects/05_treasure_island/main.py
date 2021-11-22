print("Welcome to the treasure land")

choice1 = input("You are at a crossroad and you have to take a step, would you go left or right?:")

if choice1 == "right" : 
    print ("You fell into a holw and the Game is Over")

elif choice1 == "left" :
    choice2 = input("You come to a lake. There is an island in the middle of the lake, do you wait or swim?")

    if choice2 == "swim" :
        print ("You swam and angry trouts ate you. Game Over")

    elif choice2 == "wait" :
        choice3 = input("You got on a boat and reached the island, there are 3 doors, which would you pick, Red, Yellow, or Blue")

        if choice3 == "Red" :
            print("You got into a fire")

        elif choice3 == "Blue" :
            print("Beasts attacked you, Game Over")

        elif choice3 == "Yellow" :
            print("YOU WIN! CONGRATULATIONS!")

        else :
            print("Invalid Argument")

    else :
        print("Invalid Argument")

else :
    print("Invalid Argument")



