print("welcome to the Treasuer Island")

way = print(str(input("Which way do you want to go? Left or Right?: ")))
if way == "Right":
    print("game over")
elif way == "Left":
    swim = print(str(input("Do you want to swim or wait?: ")))
    if swim == "swim":
        print("game over")
    elif swim == "wait":
        doors = print(str(input("You found 3 doors. Red, Blue, Yellow. Which one should you go?: ")))
        if doors == "Red":
            print("game over")
        elif doors == "Blue":
            print("game over")
        elif doors == "Yellow":
            print("You escaped!")