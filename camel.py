
camel = input("Enter a sentance in camel case: ")

snake = ""
for uppercase in camel:
    if uppercase.isupper():
        snake += "_" + uppercase.lower()
    else:
        snake += uppercase

print (snake)
