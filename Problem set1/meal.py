def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")  

    print("breakfast time") if 7 <= time <= 8 else print("lunch time") if 12 <= time <= 13 else print("dinner time") if 18 <= time <= 19 else None

def convert(time):    
    hours, minutes = map(int, time.replace("a.m.", "").replace("p.m.", "").split(":"))

    if "a.m." in time and hours == 12:
        hours = 0

    if "p.m." in time and hours != 12:
        hours += 12

    return hours + (minutes / 60)
        
if __name__ == "__main__":
    main()