#making a daily reminder thing that responds differently depending on whether
#task is urgent and/or time bound.
#Uses match case to cater for all conditions in priority (high/medium/low)
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "low":
        print(task, "can be done later. It is not urgent")
    case "medium":
        print(task, "should be done soon. Make time for it.")
    case "high":
        print(task, "is important. Work on it as soon as you can!")
        
if time_bound == "yes":
    print("You have a deadline. Work on", task, "before time is up.")
else:
    print("There's no need to rush.", task, "has no deadline.")