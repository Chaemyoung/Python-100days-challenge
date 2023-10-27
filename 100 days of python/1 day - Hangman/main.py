import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

word = random.choice(word_list)
guesses = ["_"] * len(word)
tries = 10

while "_" in guesses and tries > 0:
    print(" ".join(guesses))
    guess = input("Guess a letter: ")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guesses[i] = guess
    else:
        print("Incorrect guess. Try again.")
        tries -= 1

print(" ".join(guesses))
if "_" not in guesses:
    print("Congratulations! You guessed the word.")
else:
    print(f"Sorry, you ran out of tries. The word was {word}.")

# word = "apple"
# guesses = ["_"] * len(word)
# tries = 10

# while "_" in guesses and tries > 0:
#     print(" ".join(guesses))
#     guess = input("Guess a letter: ")
#     if guess in word:
#         for i in range(len(word)):
#             if word[i] == guess:
#                 guesses[i] = guess
#     else:
#         print("Incorrect guess. Try again.")
#         tries -= 1

# print(" ".join(guesses))
# if "_" not in guesses:
#     print("Congratulations! You guessed the word.")

