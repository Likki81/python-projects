import random 
def player(total):
    while True:
        try:
            user_choice=int(input("enter a number between 1 and 3:"))
            if user_choice in [1,2,3]:
                break
            else:
                print("invalid input please enter a number between 1 and 3")    
        except valueError:
          printf(" invalid input please enter a integer")        
    return total+user_choice
def computer(total):
    computer_choice=random.randint(1,3)
    print(f"computer choice is:{computer_choice}")
    return total+computer_choice
total =0
while True:
     if total<21:
         total=player(total)
         print(f"total after player turn:{total}")
         if total>=21:
             print("player reached 21 so player is loose")
             print("computer is win")
             break
         total=computer(total)   
         print(f"total after computer turn:{total}")
         if total>=21:
             print("computer reached 21 so computer is loose")
             print("player is win ")
             break 
         