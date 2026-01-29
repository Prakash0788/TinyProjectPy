import calendar

print("Calendar Program")

year = int(input("Enter Year: "))
month = int(input("Enter month (1-12): "))

print("\nHere is the calendar: \n")
print(calendar.month(year, month))