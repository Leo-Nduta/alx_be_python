#making a daily reminder thing that responds differently depending on whether
#task is urgent and/or time bound.
#Uses match case to cater for all conditions in priority (high/medium/low)
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority, time_bound:
    case "low", "yes":
        print(task, "is a low priority task. Consider completing it as soon as you can.")
    case "low", "no":
        print("Note:", task, "is a low priority task. Consider completing it when you have time.")
    case "medium", "yes":
        print(task, "is a medium priority task. Consider completing it as soon as you can.")
    case "medium", "no":
        print(task, "is a medium priority task. Consider completing it when you have time.")
    case "high", "yes":
        print("Reminder:", task, "is a high priority task. Requires immediate attention!")
    case "high", "no":
        print(task, "is a high priority task. Consider doing it as soon as you can.")
