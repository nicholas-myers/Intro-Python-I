# play  rock paper scissors with a player

# Rules: rock -> scissors
#        Scissors -> paper
#        Paper -> Rock


# Flow: start program
# specify choice from user, or quit to exit
# how does the program know the user's choice
# program also makes a choice
# how does the make choice
# randomly chooses
# when both choices are made compare to determine tie or winner
# how?
# keep track of number of wins, losses and ties for user
# how?
import random
possible_choices = ["rock", "paper", "scissors"]
program_choice = random.choice(possible_choices)
wins = 0
losses = 0
ties = 0




while True:
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    print("Program chose: " + program_choice)   
    if user_choice == "quit":
        print("See you next time!")
        break

    if user_choice == "rock":
        if program_choice == "rock":
            # tie
            ties += 1
            print("Tie!")
        elif program_choice == "paper":
            # program won, user lost
            losses += 1
            print("You Lost ><!")
        elif program_choice == "scissors":
            # program lost, user won
            wins += 1
            print("You Won!")
    elif user_choice == "paper":
        if program_choice == "rock":
            # program lost, user won
            wins += 1
            print("You Won!")
        elif program_choice == "paper":
            # tie
            ties += 1
            print("Tie!")
        elif program_choice == "scissors":
            # program won, user lost
            losses += 1
            print("You Lost ><!")
    elif user_choice == "scissors":
        if program_choice == "rock":
            # user lost, program won
            losses += 1
            print("You Lost ><!")
        elif program_choice == "paper":
            # program won, user lost
            wins += 1
            print("You Won!")
        elif program_choice == "scissors":
            # tie
            ties += 1
            print("Tie!")
    else:
        print("You didn't make a valid choice")
        continue
    
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")