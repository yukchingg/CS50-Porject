def main():
    fuel_level = convert(input("Fraction: "))
    print(gauge(fuel_level))

def convert(fraction):
    while True:
        try:
            x, y = map(int, fraction.split("/"))
            if x > y:
                raise ValueError    
            elif type(x) != int or type(y) != int:
                raise ValueError     
            return x/y*100           
        except (ValueError, ZeroDivisionError):
            fraction = round(input("Fraction: "))


def gauge(percentage):
    if percentage >= 99:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()



