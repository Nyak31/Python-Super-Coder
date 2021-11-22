

# while winning < 8
#     print winning

# if winning < 8 :
#     print("Too Low")

# if winning > 8 :
#     print("Too High")

# if winning == 8 :
    # print("Yay, you win")

game_over = False

while not game_over:
    winning = int(input("Can you guess the winning number? "))
    if winning == 8 :
        print("Yay, you win")
        game_over = True
    else:
        if winning < 8 :
            print("Too Low")
        else:
            print("Too High")

