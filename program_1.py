
# List of available events (like a small library)
events = ["Coding Workshop", "Roblox Tournament", "Science Fair", "Music Festival"]

print("=== Event Registration Program ===")

# Main loop
while True:
    # Get user info
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Display event list
    print("\nAvailable Events:")
    for i, event in enumerate(events, start=1):
        print(f"{i}. {event}")

    # Event choice
    choice = int(input("Choose an event number: "))

    # Validate choice
    if 1 <= choice <= len(events):
        selected_event = events[choice - 1]
        print(f"\n✔ {name}, age {age}, successfully registered for **{selected_event}**!\n")
    else:
        print("\n✘ Invalid event number. Please try again.\n")

    # Ask to continue
    repeat = input("Do you want to register another person? (yes/no): ").lower()
    if repeat != "yes":
        print("\nThank you for using the Event Registration Program!")
        break



# List of available events (like a small library)
events = ["Coding Workshop", "Roblox Tournament", "Science Fair", "Music Festival"]

print("=== Event Registration Program ===")

# Main loop
while True:
    # Get user info
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Display event list
    print("\nAvailable Events:")
    for i, event in enumerate(events, start=1):
        print(f"{i}. {event}")

    # Event choice
    choice = int(input("Choose an event number: "))

    # Validate choice
    if 1 <= choice <= len(events):
        selected_event = events[choice - 1]
        print(f"\n✔ {name}, age {age}, successfully registered for **{selected_event}**!\n")
    else:
        print("\n✘ Invalid event number. Please try again.\n")

    # Ask to continue
    repeat = input("Do you want to register another person? (yes/no): ").lower()
    if repeat != "yes":
        print("\nThank you for using the Event Registration Program!")
        break
