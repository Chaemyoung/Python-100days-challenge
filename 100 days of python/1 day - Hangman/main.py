import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)

def hangman():
    tries = 10
    word = chosen_word
    underscores = "_" * len(word)
    print(underscores)
    for i in range(tries):
        user_letter = input(f"Guess the letter! You have {tries - i} tries: ")
        for w in word:
            if user_letter == w:
                print("it is currect!")
                tries == tries
            elif user_letter != w:
                print("You are wrong")
                tries -= 1
            elif tries == 0:
                print("NO MORE CHANCES")
            else:
                print("What did you do? the code is broke")

if __name__ == '__main__':
    hangman()

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
# else:
#     print(f"Sorry, you ran out of tries. The word was {word}.")
