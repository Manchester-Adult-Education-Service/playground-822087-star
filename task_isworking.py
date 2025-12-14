# -------------------------------------------
# Exercise 0: Assessment Preparation (Answers)
# -------------------------------------------

# -------------------------------------------
# Task 1: Setting Up Data Storage
# -------------------------------------------

# Create an empty list to store multiple tasks
# Each task will later be a dictionary with name, priority and status
tasks = []

# Print the empty list so we can see what it looks like initially
print(tasks)


# -------------------------------------------
# Task 2: Creating a Welcome Message
# -------------------------------------------

# Print a visual title header made from equals signs
print("=======================================")
# Print the name of the system
print("TASK MANAGER SYSTEM")
# Describe what the program does for the user
print("Keep track of your daily tasks")
# Print another visual divider
print("=======================================")
# Print a blank line for spacing
print()


# -------------------------------------------
# Task 3 & Task 4: Creating the Menu & Looping It
# -------------------------------------------

# Set 'choice' to a default value so the loop starts
choice = "0"

# Use a WHILE loop so the menu repeats until the user chooses Exit
while choice != "5":

    # Display menu options each time the loop runs
    print("1. Add task")
    print("2. View all tasks")
    print("3. Search for task")
    print("4. View statistics")
    print("5. Exit")
    print()  # Blank line for spacing

    # Ask the user to pick an option and store their answer
    choice = input("Select an option: ")
    print()  # Another blank line for neatness

    # -------------------------------------------
    # Task 5: Validating Menu Input
    # -------------------------------------------

    # If the user types something invalid, keep asking until they choose a correct option
    while choice not in ["1", "2", "3", "4", "5"]:
        print("ERROR: Invalid choice")    # Inform the user the option is incorrect
        print()

        # Show the menu again so the user has another chance
        print("1. Add task")
        print("2. View all tasks")
        print("3. Search for task")
        print("4. View statistics")
        print("5. Exit")
        print()

        # Ask again for another option
        choice = input("Select an option: ")
        print()


    # -------------------------------------------
    # Task 6, 7 & 8: Adding Option 1 - Add Task, Validate & Store
    # -------------------------------------------
    if choice == "1":
        # Ask the user for the task name
        task_name = input("Enter task name: ")

        # Validation: do not allow an empty task name
        while task_name == "":
            print("ERROR: Task name cannot be blank")
            task_name = input("Enter task name: ")

        # Ask for the task priority
        priority = input("Enter priority (High/Medium/Low): ")

        # Validation: do not allow an empty priority field
        while priority == "":
            print("ERROR: Priority cannot be blank")
            priority = input("Enter priority (High/Medium/Low): ")

        # Create a dictionary to store the task information
        task = {
            "name": task_name,
            "priority": priority,
            "status": "Not started"     # Automatically added default value
        }

        # Add the new task record to the list
        tasks.append(task)

        # Confirm completion
        print()
        print("Task added successfully")
        print()


    # -------------------------------------------
    # Task 9: Adding Option 2 - View All Tasks
    # -------------------------------------------
    elif choice == "2":
        # If no tasks exist yet, display a message
        if len(tasks) == 0:
            print("No tasks recorded yet")
            print()
        else:
            # Print a header
            print("All tasks:")
            print()

            # Loop through each dictionary in the tasks list and display details
            for task in tasks:
                print(f"Name: {task['name']}")
                print(f"Priority: {task['priority']}")
                print(f"Status: {task['status']}")
                print("---------------------------------------")   # Visual divider
            print()


    # -------------------------------------------
    # Extension 1: Adding Option 3 - Search Feature
    # -------------------------------------------
    elif choice == "3":
        # If the list is empty, searching is pointless
        if len(tasks) == 0:
            print("No tasks to search")
            print()
        else:
            # Ask which task the user wants to search for
            search_name = input("Enter task name to search for: ")

            found = False   # Variable to track whether a match exists

            # Loop through all tasks to find matches
            for task in tasks:
                if task["name"] == search_name:
                    # Display the task details if found
                    print()
                    print("Task found:")
                    print(f"Name: {task['name']}")
                    print(f"Priority: {task['priority']}")
                    print(f"Status: {task['status']}")
                    print()
                    found = True

            # If after searching no match was found:
            if found == False:
                print()
                print("No matching tasks found")
                print()


    # -------------------------------------------
    # Extension 2: Option 4 - Summary Statistics
    # -------------------------------------------
    elif choice == "4":

        # If there are no tasks, there is nothing to count
        if len(tasks) == 0:
            print("No tasks to calculate statistics")
            print()
        else:
            # Create counters starting at zero
            high_count = 0
            medium_count = 0
            low_count = 0

            # Loop through every task and count according to priority
            for task in tasks:
                if task["priority"] == "High":
                    high_count += 1
                elif task["priority"] == "Medium":
                    medium_count += 1
                elif task["priority"] == "Low":
                    low_count += 1

            # Display results
            print("Task Statistics:")
            print(f"Total tasks: {len(tasks)}")
            print(f"High priority: {high_count}")
            print(f"Medium priority: {medium_count}")
            print(f"Low priority: {low_count}")
            print()


    # -------------------------------------------
    # Task 10: Adding Option 3 (now Option 5) - Exit
    # -------------------------------------------
    elif choice == "5":
        # Friendly exit message
        print("Thank you for using the Task Manager")
        print("Goodbye")
        print()

