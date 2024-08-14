import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_game():
    # Initialize scores
    user_score = 0
    computer_score = 0
    
    while True:
        # Prompt user for their choice
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue
        
        # Get computer's choice
        computer_choice = get_computer_choice()
        
        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        
        # Display choices and result
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        if result == 'tie':
            print("It's a tie!")
        elif result == 'user':
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1
        
        # Display scores
        print(f"Score - You: {user_score} | Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("Thanks for playing!")
    
# Start the game
play_game()
