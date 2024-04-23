# If the greeting starts with “hello”, output $0. 
# If the greeting starts with an “h” (but not “hello”), output $20. 
# Otherwise, output $100. 
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main():
    payment = money(input("Greeting: ").lower())
    print(f"${payment}")

def money(greeting):
    return("0") if greeting == "hello" else ("20") if greeting[0] == "h" else ("100")

if __name__ == "__main__":
    main()