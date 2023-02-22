def main():

    '''prompts the user for a time and outputs whether it's breakfast, lunch or dinner'''
    # prompt user for time
    tme = input()

def convert(time):
    '''converts a time in a 24 hour format to the corresponding number of hours'''
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()