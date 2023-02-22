#user input
user_input = input("What is the answer to the great question of Life, the Universe, and Everything?: ")

#convert input to string
answer = str(user_input)

#conditional statement to check if the asnwer is correct or not
if answer == "42":
   print("Yes")
elif answer == "forty two":
   print("Yes")
elif answer == "forty-two":
   print("Yes")
else:
   print("no")