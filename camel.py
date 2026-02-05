
camel = input("Enter a sentance in camel case: ").lower()


for upper in camel:
    if upper.isupper():
        camel = camel.replace (upper, "_" + upper.lower())

print (camel)



