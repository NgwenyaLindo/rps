import random

while True:
    play = input("enter your choice: ")


    if play == "stop":
        break

    if play != "rock" and play != "scissors" and play != "paper" :
        print("wrong input! Try again")
        continue

    options = random.choice(["rock", "paper", "scissors"])
    print(f"The computer chose {options}")

    if play == options:
        print("Draw ! , try again.....")
    elif play == "rock" and options == "scissors":
        print("Congratulations the THE USER WINS!")
        break
    elif play == "scissors" and options == "paper":
        print("Congratulations the THE USER WINS!")
        break
    elif play == "paper" and options == "rock":
        print("Congratulations the THE USER WINS!")
        break
    else:
         print("Sorry! the THE COMPUTER WINS!")

         