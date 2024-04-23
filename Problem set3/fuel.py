while True:
    try:
        fraction = input("Fraction: ")
        x, y = map(int, fraction.split("/"))

        if x > y:
            raise ValueError
        
        result = x/y
        break
    except (ValueError, ZeroDivisionError):
        pass

if result >= 0.99:
    print("F")
elif result <= 0.01:
    print("E")
else:
    print(f"{x/y:.2%}")