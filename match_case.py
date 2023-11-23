# Match Case - Switch Case
# 0 - Monday
# 1 - Tuesday
# ...
# ...

day = 10

match day:
    case 0:
        print("Monday")
    case 1:
        print("Tuesday")
    case 2:
        print("Wednesday")
    case _:
        print("Invalid Input")

# 0, 1, 2, 3, 4 - Weekday
# 5, 6 - Weekend

match day:
    case 0 | 1 | 2 | 3 | 4:
        print("Weekday")
    case 5 | 6:
        print("Weekend")
    case _:
        print("Invalid Input")