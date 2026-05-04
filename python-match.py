day = input("Enter a number (1-7) for the day of the week: ")
day = int(day)  # Ensure the input is an integer
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

day = "Sunday Saturday monday".lower()  # Convert input to lowercase for case-insensitive matching
list_of_days = day.split()  # Split the input into a list of days
first_day = list_of_days[2]  # Get the first day from the list
match first_day:
    case "sunday" | "saturday":
        print("it's Weekend!")
    case _:
        print("it's Weekday!")