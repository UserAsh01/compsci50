# Program that includes a convert function that replaces :) with 🙂 and :( with 🙁,
# and a main function that prompts the user for input, calls convert on that input, and prints the result

def convert(input_str):
    output_str = input_str.replace(":)", "🙂")
    output_str = output_str.replace(":(", "🙁")
    return output_str

def main():
    input_str = input("please enter a string: ")
    output_str = convert(input_str)
    print(output_str)

if __name__ == "__main__":
    main()