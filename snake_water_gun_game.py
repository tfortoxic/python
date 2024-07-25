def win_or_not(player, computer):
    # Rules for determining the winner
    if player == computer:
        return 0  # Draw
    elif player == "s" and computer == "w":
        return 1  # Player wins
    elif player == "w" and computer == "g":
        return 1  # Player wins
    elif player == "g" and computer == "s":
        return 1  # Player wins
    else:
        return -1  # Computer wins or invalid input

# Computer input randomization
import random
computer_choice = random.choice(["s", "w", "g"])


# Player input
player_choice = input("Enter your choice: s for snake, w for water, g for gun\n")
player_choice = player_choice.lower()

result = win_or_not(player_choice, computer_choice)

# Display the result
if result == 0:
    print("It's a draw!")
elif result == 1:
    print("You win!")
elif result == -1:
    print("Computer wins!")
else:
    print("Invalid input. Please enter s, w, or g.")