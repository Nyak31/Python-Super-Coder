# Write a program to ask 5 question to the user and ask the 
# answer in yes or no.

PC = input("The PC will ask you 5 questions, answer them correctly: this is two digit no. : 12? [yes/no]")


if PC == "yes":
    print ("you are right")
    India = input("Is india largest democratic country? [yes or no]")

    if India == "yes":
        print ("you are right")
        Snowfall = input("Is snowfall existing in sahara desert? [yes or no]")

        if Snowfall == "no":
            print ("you are right")
            sport = input("National sport of India is football? [yes or no]")

            if sport == "no" :
                print ("you are right")
                flower = input("National flower of India is rose? [yes or no]")

                if flower == "yes" :
                    print ("You are right")

else PC == "no" :
    print ("you are wrong")    
    India = input("Is india largest democratic country? [yes or no]")

    if India == "no" :
        print ("you are wrong")   


        elif flower == "no" :
                    print ("you are wrong")

            elif sport == "yes" :
                print ("you are wrong")    


        elif Snowfall == "yes" :
            print ("you are wrong")    

   