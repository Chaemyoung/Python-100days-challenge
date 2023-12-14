play = True
print("Welcome to the Secret Auction")

while play == True:
    # Ask user name
    user_name = input("what is your name?: ")

    # Ask for Bid Price
    user_bid = input("What is your Bid?: $")

    # Add Name and Bid into a dictionary as the key and value
    info_dict = {}
    info_dict[user_name] = user_bid

    # Ask if there are other users who want to bid
    play_again = input("is ther anybody who wants to bid? (Yes/No):  ").strip().lower()
    if play_again == "No":
        play = False
    else:
        continue

print("Bye Bye")
