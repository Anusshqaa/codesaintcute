import random
case=["Rock", "Paper", "Scissor"]
UserChoice=int(input("Enter your choice : 0 for Rock. 1 for Paper and 2 for Scissors- "))
print(f"User chose: {case[UserChoice]}")
Compchoice=random.randint(0,2)
print(f"Computer chose: {case[Compchoice]}")
if UserChoice >=3 or UserChoice < 0: 
    print("Invalid.")
elif Compchoice > UserChoice :
    print("You lose.")
elif Compchoice < UserChoice :
    print("You win.")
elif Compchoice==2 and UserChoice==0:
    print("You win.")
elif Compchoice==0 and UserChoice==2:
    print("You lose.")
elif Compchoice==UserChoice:
    print("Draw.")
