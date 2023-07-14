

# print("hello word!")

# print("Namrata did very well")

import random

def play_game():
    while True:
        player_choice = input("Enter your choice (rock/paper/scissors): ")
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "paper" and computer_choice == "rock")
            or (player_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

play_game()
