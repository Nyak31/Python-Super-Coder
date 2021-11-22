

print("We have to develop a fencing for plot. So please enter cost of per sq.m ; ")

Length = int(input("insert the length: "))
        
Width = int(input("insert the width: "))

Meter_cost = int(input("insert the cost(per meter): "))

# f stands for format
print(f"amount for fencing : Rs. {(((Length+Width)*2)*Meter_cost)}")