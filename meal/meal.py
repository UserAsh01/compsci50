def convert(time):
    '''converts a time in a 24 hour format to the corresponding number of hours'''
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60

def main():

    '''prompts the user for a time and outputs whether it's breakfast, lunch or dinner'''
    # prompt user for time
    time = input("What is the time? ")

    #convert time to hours
    hours = convert(time)

    #determine meal time based on time
    if 7 <= hours < 8:
        print("It's breakfast time!")
    elif 12 <+hours < 13:
        print("It's lunch time!")
    elif




if __name__ == "__main__":
    main()