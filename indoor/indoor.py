#Python program that prompts the user for input and then outputs that same input in lowercase while preserving the punctuation and whitespace

#This program first prompts the user to enter a string by calling the input() function and passing in a prompt string. It then stores the user's input in the input_str variable.
#The program then calls the lower() method on the input_str variable to convert it to lowercase, and stores the result in the lowercase_str variable.
#Finally, the program uses the print() function to output the lowercase version of the user's input, while preserving any punctuation and whitespace.

input_str = input("Please enter a string: ")
lowercase_str = input_str.lower()
print(lowercase_str)
