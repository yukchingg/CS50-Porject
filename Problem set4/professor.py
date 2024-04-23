import random


def main():
    chosen_level = get_level()
    score = 0
    for _ in range(10):
        num1 = generate_integer(chosen_level)
        num2 = generate_integer(chosen_level)
        i = 0
        while i <3:
            try:
                reply = int(input(f"{num1} + {num2} = "))
                if reply != (num1 + num2):
                    raise ValueError
                score += 1
                break
            except ValueError:
                print("EEE")
                i +=1           
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if not (level == 1 or level == 2 or level == 3):
                raise ValueError
            break
        except ValueError:
            pass
    return level


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()