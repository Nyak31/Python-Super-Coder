## Output : 

"""

Hey! You are already done with your final exams of class 10

Go ahead and insert the marks you acheieved in each subject which the computer will ask.

Here we go!

Algebra .../100 : 95
Geometry .../100 : 98
Physics .../100 : 100
Chemistry .../100 : 65
Biology .../100 : 32
English .../100 : 97
Social Studies .../100 : 93

Total marks you got were 580 / 700
Percentage : 82.85

"""

print("Hey! You are already done with your final exams of class 10")
print("Go ahead and insert the marks you acheieved in each subject which the computer will ask.")
print("Here we go!")

Algebra = int(input("Algebra: .../100")) 
Geometry = int(input("Geometry: .../100 "))
Physics = int(input("Physics: .../100 "))
Chemistry = int(input("Chemitry: .../100 "))
Biology = int(input("Biology: .../100 "))
English = int(input("English: .../100 "))
Social_Studies = int(input("Social Studies: .../100 "))

print(f"Total marks you got were: {Algebra+Geometry+Physics+Chemistry+Biology+English+Social_Studies}")
print(f"Percentage : {round((Algebra+Geometry+Physics+Chemistry+Biology+English+Social_Studies)/7, 2)}")

#loops next section - learn about loops and revise