import random

while True:
    try:
        number = int(input("Level: "))
        if number <= 0:
            raise ValueError
        break
    except ValueError:
        pass

answer = random.randint(1, number)

while True:
    guess = int(input("Guess: "))
    if guess == answer:
        print("Just right!")
        break
    elif guess > answer:
        print("Too large!")
    else:
        print("Too small!")

