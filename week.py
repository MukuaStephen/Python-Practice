day = input("Enter a day of the week") .lower()

match day:
    case "monday":
        print("Today is Monday. Ugh, Mondays...")
    case "tuesday":
        print("Today is Tuesday. Just another workday! Almost to Wednesday...")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost There...")
    case "friday":
        print("It's Friday! The weekend is almost here! TGIF!")
    case "saturday" | "sunday":
        print("The weekend vibes! Time to relax and have some fun!")
    case _:
        print("Invalid day. Please enter a valid day of the week.")
        