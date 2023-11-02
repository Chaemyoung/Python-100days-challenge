import random

AI_list = ["Rock", "Paper", "Scissors"]
AI_choice = random.choice(AI_list)

print("Welcome to Rock-Paper-Scissors")
user_choice = input("What do you choose? Type Rock or Paper or Scissors.: ")
print(user_choice)
if user_choice == "Rock" or "rock":
    if AI_choice == "Rock":
        print(f"You: {user_choice} - AI: {AI_choice}")
        print("Draw")
    elif AI_choice == "Paper":
        print(f"You: {user_choice} - AI: {AI_choice}")
        print("You Lost")
    elif AI_choice == "Scissors":
        print(f"You: {user_choice} - AI: {AI_choice}")
        print("You Won")
elif user_choice == "Paper" or "paper":
    if AI_choice == "Rock":
        print(f"You: {user_choice} - AI: {AI_choice}")
        print("You Won")
    elif AI_choice == "Paper":
        print(f"You: {user_choice} - AI: {AI_choice}")
        print("Draw")
    elif AI_choice == "Scissors":
        print(f"You: {user_choice} - AI: {AI_choice}")
        print("You Lost")
elif user_choice == "Scissors" or "scissors": 
    if AI_choice == "Rock":
        print(f"You: {user_choice} - AI: {AI_choice}")
        print("You Lost")
    elif AI_choice == "Paper":
        print(f"You: {user_choice} - AI: {AI_choice}")
        print("You Won")
    elif AI_choice == "Scissors":
        print(f"You: {user_choice} - AI: {AI_choice}")
        print("Draw")