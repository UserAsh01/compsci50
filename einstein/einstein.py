#Python program that prompts the user for mass in kilograms and then calculates the equivalent energy in Joules
# using the equation E=mc^2, where c is the speed of light:
c = 300000000 #speed of light in meters per second
m = int(input("Enter mass in kilograms: "))
E = m * c**2
print("Energy in Joules:", E)
