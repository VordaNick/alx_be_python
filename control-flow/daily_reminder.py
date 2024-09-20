task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        message = "high priority task"
        
    case "medium":
        message = "medium priority task"
        
    case "low":
        message = "low priority task"
    
if time == "yes":
    message += " that requires immediate attention today!"
print(f"{task} is a {message}")
    
