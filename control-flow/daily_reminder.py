task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        if time == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        elif time == "no":
            print(f"'{task}' is a high priority task but does not require immediate attention")
    case "medium":
        if time == "yes":
            print(f"'{task}' is a medium priority task but requires immediate attention today!")
        elif time == "no":
            print(f"'{task}' is a medium priority task and does not require immediate attention")
    case "low":
        if time == "yes":
            print(f"'{task}' is a low priority task but requires immediate attention today!")
        elif time == "no":
            print(f"'{task}' is a low priority task that does not require immediate attention.")
