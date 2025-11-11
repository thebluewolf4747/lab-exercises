def prep_exercise_1():
    player_health = 100

    def take_damage(player_health):
        player_health -= 20
        return player_health

    player_health = take_damage(player_health)

def prep_exercise_2():
    total_actions = 0
    player_level = 1

    while player_level < 4:
        print(f"Processing Level {player_level}...")

        # Nested for loop
        for action in range(player_level):
            total_actions += 1
        
        player_level += 1
    
    return total_actions

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

def exercise_1():
    # String slicing and .split() exercise
    log_data = "SCORE:Player_1:2500"
    parsed_data = log_data.split(":")
    player_name = parsed_data[1]
    player_score = parsed_data[2]

    return player_name, player_score

def exercise_2():
    # Lists exercise (quiz)
    questions = ["What is 2 + 2? ", "What is the capital of France? ", "What keyword defines a function? "]
    answers = ["4", "Paris", "def"]
    score = 0

    for i in range(len(questions)):
        user_answer = input(questions[i])
        if user_answer == answers[i]:
            score += 1
    
    return f"Final Score: {score}"

def exercise_3():
    phonebook = {}
    phonebook["Alice"] = "555-1234"
    phonebook["Bob"] = "555-5678"

    name = input("Who do you want to look up? ")

    print(phonebook[name])

    phonebook["Charlie"] = "555-9999"

    for name, num in phonebook.items():
        print(f"Name: {name}, Number: {num}")
