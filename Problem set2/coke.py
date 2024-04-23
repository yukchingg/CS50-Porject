due = 50

while due > 0:
    print(f"Amount due: {due}")
    coin = int(input("Insert coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        due -= coin

print(f"Change owed: {abs(due)}")