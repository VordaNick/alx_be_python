task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        print(f"'{task}' is a {priority} priority task")
    case "medium":
        print(f"'{task}' is a {priority} priority task")
    case "low":
        print(f"'{task}' is a {priority} priority task")
if time == "yes":
    print(f"'{task}' is a {priority} priority task that requires immediate action today!")
    
