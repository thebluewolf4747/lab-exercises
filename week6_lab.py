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
# total_actions = 0
# player_level = 1

# # A while loop that runs for levels 1, 2, and 3
# while player_level < 4:
#     print(f"Processing Level {player_level}...")

#     # A nested for loop that runs 'player_level' times
#     # e.g., for level 3, it runs 3 times (0, 1, 2)
#     for action in range(player_level):
#         total_actions = total_actions + 1
    
#     player_level += 1

# print(f"Total actions: {total_actions}")


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

""" Exercise 1: String Slicing & .split() """

# log_data = "SCORE:Player_1:2500"
# parsed_data = log_data.split(":")
# # Print whole list
# print(parsed_data)
# # Print player's name only
# print(parsed_data[1])
# # Print score only
# print(parsed_data[2])

""" Exercise 2: Lists - The Quiz """

# questions = ["What is 2 + 2? ", "What is the capital of France? ", "What keyword defines a function? "]
# answers = ["4", "Paris", "def"]
# score = 0

# for i in range(len(questions)):
#     user_answer = input(questions[i])
#     if user_answer == answers[i]:
#         print("Correct!")
#         score += 1
#     else:
#         print("Wrong!")

# print(f"Final Score: {score}")

""" Exercise 3: Dictionaries - The Phonebook """

phonebook = {}
phonebook["Alice"] = "555-1234"
phonebook["Bob"] = "555-5678"

name = input("Who do you want to look up? ")

print(phonebook[name])

phonebook["Charlie"] = "555-9999"

for name, num in phonebook.items():
    print(f"Name: {name}, Number: {num}")