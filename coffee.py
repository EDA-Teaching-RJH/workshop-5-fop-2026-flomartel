# statement of requirements:

# functional requirements:
# accepts 50, 20, 10, 5 as integers, doesnt accept strings

# non-functional requirements:
# if the user inputs a string the system should ask again for an integer input instead of crashing


amount_due = 75
print ("Amount Due: 75p")

while amount_due > 0:
    coin = int(input("Please insert a coin (50, 20, 10 or 5): "))
    
    if coin == 5 or coin == 10 or coin == 20 or coin == 50:
        amount_due -= coin
        print ("Amount still due:",amount_due)

if amount_due < 0:
    print("Change due:", abs(amount_due))
else:
    print("No change due")
