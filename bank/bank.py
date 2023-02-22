#prompt user for greeting
greeting = input("Please enter a greeting: ")

#remove leading whitespace and convert to lowercase
greeting = greeting.lstrip().lower()

#Check first letter of greeting and output corresponding value
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
