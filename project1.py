name = input("Hey  type your name : ")
print("Hello", name, "welcome to my game!")

should_we_play = input("Do you want to play?\n").lower()

while should_we_play == "yes" or should_we_play == "y":
    print("\n*** We are gonna play ***")
    direction = input("You are at a fork in the road. Do you want to go left, right, forward, or backward? ").lower()

    if direction == "left":
        print("You went left and fell off a cliff. GAME OVER!")
    elif direction == "right":
        print("You went right and found a treasure chest! 🎉")
    elif direction == "forward":
        print("You went forward and met a dragon! 🐉")
        choice = input("Do you wanna fight the dragon ? (yes/no) ").lower()
        if choice == "y" or choice == "yes":
            print("You fought thr Dragon... YOU DIEDDD ")
        else:
            print("Dragon let you pass... This time... Good Decision")
    elif direction == "backward":
        print("You went backward and returned to the village safely. 🏡")
    else:
        print("SORRY, not a valid reply. You got lost in the wilderness. YOU DIEEEE! 💀")

    should_we_play = input("\nWanna try again? (yes/no) : ").lower()

print("***Thank you for playing the game***") 