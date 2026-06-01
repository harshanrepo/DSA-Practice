# choice=int(input("Enter your choice (1-3): "))

# match choice:
#     case 1:
#         print("Nice Choice..")
#     case 2:
#         print("Not bad..")
#     case 3:
#         print("Not a wise choice my lord..")

Day=input("Enter your day: ")

match Day:
    case "Monday":
        print("Today is Monday..")
    case "Tuesday":
        print("Today is tuesday..")
    case "Wednesday":
        print("Today is wednesday..")
    case "Thrusday":
        print("Today is Thrusday..")
    case "Friday":
        print("Today is Friday..")
    case "Saturday":
        print("Today is Saturday..")
    case "Sunday":
        print("Today is Sunday..")
    case _:
        print("Please check the spelling again..")

