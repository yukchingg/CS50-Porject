def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return(
        length(s)
        and first_two_digits(s)
        and no_symbols(s)   
        and no_first_zero(s)
        and no_mid_digit(s)
    )

def length(s):
    return 2 <= len(s) <= 6
    
def no_first_zero(s):
    for ch in s:
        if ch.isdigit() and ch == "0":
            return False
    return True

def no_mid_digit(s):
    digit_flag = False

    for ch in s:
        if ch.isdigit():
            digit_flag = True
        if ch.isalpha() and digit_flag:
            return False
    return True

def first_two_digits(s):
    return s[0:2].isalpha()

def no_symbols(s):
    return s.isalnum()

main()