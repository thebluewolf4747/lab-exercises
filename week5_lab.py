def start_scene():
    choice1 = input("You are in a dark forest. You see two paths. Do you go 'left' or 'right'?")
    if choice1 == "l" or choice1 == "L" or choice1 == "left" or choice1 == "Left":
        left_path_scene()
    
    elif choice1 == "r" or choice1 == "R" or choice1 == "right" or choice1 == "Right":
        right_path_scene()
    
    else:
        print("Invalid Choice")

def left_path_scene():
    choice2 = input("You walk down the left path and find a river. Do you swim across or follow the river bank? ")
    if choice2 == "s" or choice2 == "S" or choice2 == "swim" or choice2 == "Swim":
        swim_scene()
    
    elif choice2 == "f" or choice2 == "F" or choice2 == "follow" or choice2 == "Follow":
        follow_scene()
    
    else:
        print("Invalid Choice")

def right_path_scene():
    choice2 = input("You walk down the right path and encounter a sleeping bear. Do you tiptoe past or run away? ")
    if choice2 == "t" or choice2 == "T" or choice2 == "tiptoe" or choice2 == "Tiptoe":
        print("You successfully sneak past the bear. You win!")
    
    elif choice2 == "r" or choice2 == "R" or choice2 == "run" or choice2 == "Run":
        print("You trip while running and the bear wakes up. You lose.")
    
    else:
        print("Invalid Choice")

def swim_scene():
    print("You are tired from swimming and rest. You win!")

def follow_scene():
    print("You follow the river bank and find a hidden cave. You win!")


start_scene()