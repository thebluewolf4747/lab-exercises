player_health = 100

def take_damage(player_health):
    player_health = player_health - 20
    print("Player took damage!")
    return player_health

# Function is called, but the new value is never returned or assigned
player_health = take_damage(player_health)

print(f"Player health is: {player_health}")
# Expected output: Player health is: 80
# Actual output: Player health is: 100