months = {
    "January": 1, "February": 2, "March": 3,
    "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9,
    "October": 10, "November": 11, "December": 12
}

while True:
    x = input("Date: ")
    if "/" in x:
        try:
            month, day, year = x.split("/")
            month, day, year = int(month), int(day), int(year)
        except ValueError:
            continue
    else:
        try:
            d, year = x.split(", ")
            month, day = d.split(" ")
            day = int(day)
            month = months[month]
            year = int(year)
        except (ValueError, KeyError):
            continue
    if 1 <= month <= 12 and 1 <= day <= 31:
        print(f"{year}-{month:02d}-{day:02d}")
        break