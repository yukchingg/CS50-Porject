stored = {}

while True:
    try:
        item = input().upper()
    except EOFError:
        break

    if item in stored:
        stored[item] += 1
    else:
        stored[item] = 1

for item, count in stored.items():
    print(f"{count} {item}")
