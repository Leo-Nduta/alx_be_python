#making a daily reminder thing that responds differently depending on whether
#task is urgent and/or time bound.
#Uses match case to cater for all conditions in priority (high/medium/low)
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "low":
        priority_msg = f"{task} is a low priority task."
    case "medium":
        priority_msg = f"{task} is a medium priority task."
    case "high":
        priority_msg = f"{task} is a high priority task."

if time_bound == "yes":
    time_bound_msg = ("Work on it as soon as you can.")
else:
    time_bound_msg = ("Consider working on it when you have time.")
    
print(f"Reminder: {priority_msg}{time_bound_msg}")