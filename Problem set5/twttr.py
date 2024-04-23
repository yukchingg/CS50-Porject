def main():
    print(shorten(input("Input: ")))

def shorten(original):
    vowels = "aeiouAEIOU"
    return "".join([ch if ch not in vowels else "" for ch in original])

if __name__ == "__main__":
    main()