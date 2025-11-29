#
# List of available events (like a small library)
events = ["Coding Workshop", "Roblox Tournament", "Science Fair", "Music Festival"]
event_comer=[]
print("=== Event Registration Program ===")

# Main loop
while True:
    # Get user info
    name = input("Enter your name       : ")
    age  = int(input("Enter your age    : "))
if age <=10 :
    print ("sorry you cannot participate this event because you are too young ")
break
#clear
else:
print ("you can can chose your event ")
    
for i. Event in event_comer:

    participant = { 
                    "name"  : name,
                    "event" : selected_event,
                    "age "  : "age",
        }

    event_comer.append(participant)

    # Display event listparticipant
    
    print("\nAvailable Events:")
    i=0
    
    for  event in enumerate(events, start=1):
        print(f"{i}. {event}")

    # Event choice
    choice = int(input("Choose an event number: "))

    # Validate choice
if 1 <= choice <= len(events):
        selected_event = events[choice - 1]
else:
        print("\n✘ Invalid event number. Please try again.\n")

        print("================== who else comming for events list ==========================================\n")
        print("======   NAME.        AGE                                              SELECTED EVENT.   •••• \n")
        print("================================================================================================")
        print("\n--- Registered Participants ---")

if event_comer:
    for event in event_comer():
        print(event_comer())
        print(f"Name: {participant['name']},Event: {participant['event_choice']},Age: {participant['age']}")
else:
    print("No participants registered.")
    #return event_comer()

if event_comer:
        #for event in event_comer:
            print(f"\n✔ {name}    , age :   {age}     , successfully registered for   **.    {selected_event}     **!\n")
else:
    print("  No participants reggistered. ")

###Ask to continu

repeat = input("Do you want to register another person? (yes/no): ").lower()
if repeat != "yes":
    values=event_comer.values()

    print (event_comer.get("name"))

    print("\n THANK YOU FO.R USING THE EVENT REGISTRATION PROGRAM!\n") 

    #break
#clear



##########if participants_list:

    #for participant in participants_list:
        #print(f"Name test: {participant['name']}, Age: {participant['age']}, Event: {participant['event_choice']} \n")
    #else:
        #print("No participants registered.")

    ####return participants_list




