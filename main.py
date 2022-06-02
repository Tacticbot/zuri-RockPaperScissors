import random

def start_game(player_action, computer_action):

    if player_action == "R":
        if computer_action == "S":
            print("Rock smashes Scissors! You win")
        else:
            print("Paper covers Rock! You lose")
    elif player_action == "P":
        if computer_action == "R":
            print("Paper covers Rock! You win")
        else:
            print("Scissors cuts Paper! You lose")
    elif player_action == "S":
        if computer_action == "P":
            print("Scissors cuts Paper! You win")
        else:
            print("Rock smashes Scissors! You lose")
    
print("Welcome to Rock, Paper, Scissors")   

while True:

    while True:

    
        possible_input = ["R", "P", "S"]
        computer_action = random.choice(possible_input)
        
        player_action = input("Input a choice 'R', 'P' or'S'?: ")

    
        if player_action not in possible_input or len(player_action)>1:
            print("Invalid input: Please enter a valid input")
            continue
        else:
            break
    
    print(f"\nYour choice is {player_action}, the computer choice is {computer_action}.\n")

    if player_action == computer_action:
        print(f"Its a tie, Both players selected {player_action}")
        print("Lets start Over")
        continue

    start_game(player_action, computer_action) 
    play_again = input("Do you wish to play again (y/n): ") 
    if play_again == "y":
        continue
    else:
        print("Great game!")
        break


