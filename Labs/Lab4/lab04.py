# Import the random library to use for the dice later
import random

#Lab 4 START
#Monster power dict
monsterPowers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

#Update monster power
def monsterStrengthUpdate():
    powerName = random.choice(list(monsterPowers.keys()))
    strength = monsterPowers[powerName]
    m_combat_strength = min(strength, 6)
    print(f"Selected power: {powerName}; Strength: {m_combat_strength}\n")
    return m_combat_strength
#Empty belt
belt = []


# Game
# Define The number of lives for the Hero and Monster
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

# Define the Dice
diceOptions = list(range(1, 7))
# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Print out the weapons using a for loop
for weapon in weapons:
    print(weapon)

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]

m_combat_strength = monsterStrengthUpdate()
print(m_combat_strength)

input("Roll the dice for your health points (Press enter)")
health_points = random.choice(diceOptions)
print("Player rolled " + str(health_points) + " health points")

print("\nYou found loot!")
input("Press any key to roll: ")
loot_selected = random.choice(loot_options)
loot_options.pop(loot_options.index(loot_selected))
belt.append(loot_selected)
print(f"Belt items: {belt}\n")

print("You found another loot!")
input("Press any key to roll: ")
loot_selected = random.choice(loot_options)
loot_options.pop(loot_options.index(loot_selected))
belt.append(loot_selected)
print(f"Belt items: {belt}\n")

print("Monster encountered, using first loot item...")
item_selected = belt[0]
belt.pop(0)

print(f"Item used: {item_selected}")
if item_selected in good_loot_options:
    health_points = min (6, health_points + 2)
    print("That was useful!")
elif item_selected in bad_loot_options:
    health_points = max (0, health_points - 2)
    print("That was awful!")
else:
    print("...That was not helpful...")
print(f"Updated health: {health_points}")