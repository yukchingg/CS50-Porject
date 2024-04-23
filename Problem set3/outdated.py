m = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        month, day, year = map(int, date.split("/"))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError
        break

    except ValueError: 
        pass

print(f"{year}-{month:02}-{day:02}")