""" Exercise 1 """
# player_health = 100

# def take_damage(player_health):
#     player_health = player_health - 20
#     print("Player took damage!")
#     return player_health

# # Function is called, but the new value is never returned or assigned
# player_health = take_damage(player_health)

# print(f"Player health is: {player_health}")


""" Exercise 2 """
total_actions = 0
player_level = 1

# A while loop that runs for levels 1, 2, and 3
while player_level < 4:
    print(f"Processing Level {player_level}...")

    # A nested for loop that runs 'player_level' times
    # e.g., for level 3, it runs 3 times (0, 1, 2)
    for action in range(player_level):
        total_actions = total_actions + 1
    
    player_level += 1

print(f"Total actions: {total_actions}")


"""
For player_level = 1:
for action in range(1):
    total_actions = 1

total_actions = 1
For player_level = 2:
for action in range(2):
    total_actions = total_actions + 1

total_actions = 3
For player_level = 3:
for action in range(3):
    total_actions = total_actions + 1

total_actions = 6
Final result: total_actions = 6

"""