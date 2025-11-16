def register_event_participants():
    """
    Collects participant information (name, age, event choice)
    and stores it in a list of dictionaries.
    """
    participants_list = [] # Initialize an empty list to store all participants
    
    print("--- Event Registration System ---")

    while True:
        # Prompt the user for input
        name = input("Enter participant's name (or 'quit' to exit): ").strip()
        
        if name.lower() == 'quit':
            break

        # Input age and validate it is a number
        while True:
            age_input = input(f"Enter {name}'s age: ").strip()
            try:
                age = int(age_input)
                if age <= 0:
                    print("Age must be a positive number. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input for age. Please enter a number.")

        event_choice = input(f"Enter {name}'s event choice: ").strip()

        # Create a dictionary for the new participant
        new_participant = {
            'name': name,
            'age': age,
            'event_choice': event_choice
        }

        # Append the participant's dictionary to the list
        participants_list.append(new_participant)
        print(f"\n{name} registered successfully!\n")

    # Display all registered participants
    print("\n--- Registered Participants ---")
    if participants_list:
        for participant in participants_list:
            print(f"Name: {participant['name']}, Age: {participant['age']}, Event: {participant['event_choice']}")
    else:
        print("No participants registered.")

    return participants_list

if __name__ == "__main__":
    registered_users = register_event_participants()