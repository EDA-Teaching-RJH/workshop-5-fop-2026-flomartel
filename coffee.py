
amount_due = 75
print ("Amount Due: 75p")


coin = int(input("Please insert a coin(50, 20, 10 or 5): "))

if coin == 5 or coin == 10 or coin == 20 or coin == 50:
    amount_due -= coin
    print ("Amount still due: ", amount_due)
