winning = int(input("Can you guess the winning number? "))

if winning < 8 :
    print("Too Low")

if winning > 8 :
    print("Too High")

if winning == 8 :
    print("Yay, you win")