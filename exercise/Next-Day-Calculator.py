# This Python code determines whether a given date is valid and calculates the next day.


day = int(input("enter number of day : "))
month = int(input("enter number of month : "))
year = int(input("enter number of year : "))
if 1 <= day <= 31 and 1 <= month <= 12:
    if 1 <= month <= 6:
        if day <= 30:
            print(year, month, day + 1, sep="-")
        else:
            print(year, month + 1, 1, sep="-")

    elif 7 <= month <= 11:
        if day <= 29:
            print(year, month, day + 1, sep="-")
        else:
            print(year, month + 1, 1, sep="-")

    else:
        if day <= 28:
            print(year, month, day + 1, sep="-")
        else:
            print(year + 1, 1, 1, sep="-")

    if year % 4 == 0:
        print(year, "is a leap year")
else:
   print("you entered an invalid date !!")
    print("you entered an invalid date !!")
