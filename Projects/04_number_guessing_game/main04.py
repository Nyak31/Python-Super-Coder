# Here are the imports / dependencies for this project.
from random import randint

"""You will have a winning_number variable in your python script For an eg. winning_number = 8
If the number is more than 8, it should spit out 'Its high'.
If the number is less than 8, it should spit out 'Its low'.
If the number = 8, it should say 'You win.'
If the number is either less than 1 or more than 100 then it should print out 'Its not expected.'
"""
logo = """
/ _ \_ _ ___ ___ ___ /__ \ |__ ___ /\ \ \_ _ _ __ ___ | |__ ___ _ __
/ /_\/ | | |/ _ \/ __/ __| / /\/ '_ \ / _ \ / \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| | __/\__ \__ \ / / | | | | __/ / /\ /| |_| | | | | | | |_) | __/ |
\____/ \__,_|\___||___/___/ \/ |_| |_|\___| \_\ \/ \__,_|_| |_| |_|_.__/ \___|_|
"""
print(logo)
print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")

easy_attempts = 15 #number of lives for easy level
easy_lives = 0
hard_attempts = 10 #number of lives for hard level
hard_lives = 0
winning_number = randint(1,100)

gameover = False

choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if choose_difficulty == "easy":
    while easy_lives < easy_attempts:
        user_input = input("Guess a number : ")

        if user_input == "":
            print("Its Invalid")

        elif user_input.isalpha():
            print("No Alphabets Please.")

        else:
            user_input = int(user_input)

            if user_input == winning_number:
                print("Yay, you win")
                easy_lives = easy_attempts
        
            else:
                if user_input < winning_number:
                    print("Too Low")
                else:
                    print("Too High")

        easy_lives = easy_lives + 1  # Keep running until max lives are attained.

if choose_difficulty == "hard":
    while hard_lives < hard_attempts:
        user_input = input("Guess a number : ")

        if user_input == "":
            print("Its Invalid")

        elif user_input.isalpha():
            print("No Alphabets Please.")

        else:
            user_input = int(user_input)

            if user_input == winning_number:
                print("Yay, you win")
                hard_lives = hard_attempts
            else:
                if user_input < winning_number:
                    print("Too Low")
                else:
                    print("Too High")
        
        hard_lives = hard_lives + 1  # Keep running until max lives are attained.

 #tomorrow explain how easy_lives = easy_attempts  fama
 