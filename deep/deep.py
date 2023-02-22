#user input
user_input = input("What is the answer to the great question of Life, the Universe, and Everything?: ").lower()

#account for typing variations such as spaces , cases etc
user_input = user_input.replace(" ","").replace("-","")
#convert input to string
answer = str(user_input)

#conditional statement to check if the asnwer is correct or not
if answer == "42" or answer =="fortytwo" or answer == "forty-two":
   print("Yes")

else:
   print("no")