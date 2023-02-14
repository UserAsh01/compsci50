#Python program that promtpts the user for input and then outputs the same input
#replacing each space with three periods

input_str = input("Please enter a string: ")
modified_str = input_str.replace(" ","...")
print(modified_str)