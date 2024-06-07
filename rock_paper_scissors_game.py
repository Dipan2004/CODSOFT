import random

def get_user_choice():
    
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_choice in ['rock', 'paper', 'cissors']:
        return user_choice
    else:
        print("Invalid input. Please try again.")
        return get_user_choice()

def get_computer_choice():
    
    choices = ['rock', 'paper', 'cissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'cissors') or \
         (user_choice == 'cissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    
    print(f"You chose {user_choice}. The computer chose {computer_choice}.")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

def main():
    user_score = 0
    computer_score = 0
    play_again = "yes"

    while play_again.lower() == "yes":
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score: You {user_score}, Computer {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
