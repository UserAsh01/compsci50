def camel_to_snake(name):
   """
   Converts a variable name in camel case to snake case.
   """

   snake_case_name = ""
   for i, c in enumerate(name):
    if c.isupper():
        # if the current character is upper case, add an underscore
        # and the lowercase version of the same character to the new name
        if i > 0:
            snake_case_name += "_"
        snake_case_name += c.lower()
    else:
        #otherwise, just add the character into the new name
        snake_case_name  += c
   return snake_case_name
# Prompt the user for a variable name in camel case
camel_case_name = input("camelCase: ")

# Convert the name to snake case
snake_case_name = camel_to_snake(camel_case_name)

# Print the snake case name
print("snake_case:", snake_case_name)