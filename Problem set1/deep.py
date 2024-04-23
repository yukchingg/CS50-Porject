def main():
    print(decider(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")))

def decider(Answer):
    # if Answer == "42" or Answer == "forty-two" or  Answer == "forty two":
    #     return "Yes"
    # return "No"

    return "Yes" if Answer == "42" or Answer == "forty-two" or Answer == "forty two" else "No"

if __name__ == "__main__":
    main()