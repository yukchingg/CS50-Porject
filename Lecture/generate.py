import random

# coin = random.choice(["heads", "tails"])
# print(coin)

# number = random.randint(1,10)
# print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for _ in cards:
    print(_)