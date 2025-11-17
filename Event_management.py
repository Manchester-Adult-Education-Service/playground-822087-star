## Manchester commuinity centre event management programme.
print(" \n === Welcome to the Event Registration System =====") 
participants = [] ### list to  store all paricipants.
count=0
#event_choice= " "
again=" "
#while again!="yes":
name =input("Enter your name:-")
event_choice = input("Enter event choice (Music / Dance / Sports/ yes): ")
age =int(input("Enter your Age :- "))
if age >=12:
   print("you are eligible to participate ")
else:
    print(" sorry better luck next time ")
again = input("\n Do you want to add another participant  ?:-(yes/no):").lower() 

count+=1
    ## store participant details in a dictionary ####
for event in event_choice:
     participant = { 
       "name" : name,
       "age " : age,
       "event" : event_choice,
   }
participants.append (participant)

print (f"\n This is your name:- {name} , age :- {age}  ,you are registered for the {event_choice}")
print("\nThank you for using the Event Registration System!")
###ask if user wants to continue 

#if again != "yes":
 #   loop
#else:
#reak:
print(f"\n == Event Participant ==")
p=1
for p in participants:
    print (f"name :{p['name']},age :{p['age']},event :{p['event']}")
    
p=p+1
    ##event_choice=list("stage singing show, dancing activity,magical show,coding club")
    ##event_choice=1 ##(Stage singig show")


