# If the greeting starts with “hello”, output $0. 
# If the greeting starts with an “h” (but not “hello”), output $20. 
# Otherwise, output $100. 
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main():
    money(input("Greeting: ").lower())

def money(greeting):
    # if greeting == "hello":
    #     print("$0")
    # elif greeting[0] == "h":
    #     print("20")
    # else:
    #     print("$100")

    #Short hand if
    print("$0") if greeting == "hello" else print("20") if greeting[0] == "h" else print("$100")


main()