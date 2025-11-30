    # The loop will continue running until the user selects "3" (Exit).
    #choice != "3":

    # Display the menu options clearly to the user
print()
print("========* THIS IS MANCHESTER COMMUNITY CENTRE EVENT REGISTRATION  SYSTEM *  ==========\n")
print("1.Input the Registers details ")
print("2.Disply the Success registed ")
print("3.Exit the programe ")
    
    # Get the user's menu selectionchoice = "0"
choice = "0"
choice = input("Select an option: ")
print()

    # -------------------------------------------
    # Task 3: Viewing All Books (Option 1)
    # -------------------------------------------
if choice == "1":
    print ("input")
        # Check if the l"ibrary is empty before looping (good practice)
        #if len(library) == 0:
         #   print("No books in the inventory.")
        #else:
         #   print("Current Inventory:")
          #  print("------------------")
            # Loop through every dictionary (book record) in the list
           # for book in library:
                # We use f-strings to format the output nicely.
                # We access values using their keys: book['title'], etc.
            #    print(f"Title: {book['title']} | Author: {book['author']} | Stock: {book['stock']}")
             #   print("------------------") 

    # -------------------------------------------
    # Handling Exit (Option 3)
    # -------------------------------------------
    #elif choice == "3":
     #   print("Goodbye! Closing the program.")

    # -------------------------------------------
    # Invalid Input Handling
    # -------------------------------------------
    #else:
        # If the user types "2" (because we haven't built it yet), 
        # or "hello", or "4", it comes here.
     #   print("Invalid choice (or feature coming soon). Please try again.")
    def register_event_participants():
    #Collects participant information (name, age, event choice)
    #and stores it in a list of dictionaries.
        participants_list = [] # Initialize an empty list to store all participants
        count=0
    #print("========* THIS IS MANCHESTER COMMUNITY CENTRE EVENT REGISTRATION  SYSTEM *  ==========\n")
    #print("1.Input the Registers details ")
    #print("2.Disply the Success registed ")
    #print("3.Exit the programm ")
        print()
        name=" "
    ###while True:
    while name !="quit":
        # INPUT THE USER NAME AND DETAILS 
        name = input("Enter participant's name ( (or) 'quit' to exit). : ").strip()
        #while   name =="" : 
        if name.lower() == 'quit':
            break

        # HERE INPUT AGE VALIDATE HAPPENING. IT IS A NUMBER  ..

        #while True:

        age_valid = False
    while not age_valid:
        age_valid = input(f"Enter      {name}.   's age           : ").strip()
        try:
            age = int(age_input)
            if  10 <= age <=65 :
             age_valid =True
            else:
                #if age < 5 and 15 :
                #if age < = 18:
                print("Age must be bitween 10 and 65 over  please try next time . Please try again.")
            continue
            break
        except ValueError:
                
            print("Invalid input for age. Please enter a number.")
            print()
            print("1.stage show with  karoke    ")
            print("2.coding shows.              ")
            print("3.painting shows             ")
                
            event_choice = input(f"Enter {name}'s event choice.         : ").strip()

        ###event counting #####
            event_choice ={1:0,2:0,3:0}
            
        # Create a dictionary for the new participant
            new_participant = {
            'name': name,
            'age': age,
            'event_choice': event_choice
            }

        # Append the participant's dictionary to the list

        participants_list.append(new_participant)
        print(f"\n{name} registered successfully!\n")
        #count=count+1
        #print (count)
        # Display all registered participants•••###########

        print("\n===-REGISTERED PARTICIPANTS =============================\n")
    
        print("\n Total come     .NAME.        AGE.            EVENT_CHOICE ")

        if participants_list:
            count=0
            #total =0
        for participant in participants_list:
            count=count+1
            #total=total+count
            print(f"{count}:       {participant['name']},      Age: {participant['age']},                 Event: {participant['event_choice']} \n")
            #print(total)
        for event_id , count in event_choice.items(): 
            if count > 0:
                print (f/ "{events[event_id]}: {count} participant(s)")
            else:
                print(" No participants registered.")
        #print(total)
    return participants_list
if __name__ ==  "__main__":
    registered_users = register_event_participants()


        
