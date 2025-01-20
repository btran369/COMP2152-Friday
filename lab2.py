import random

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
def main():
    try:
        weaponRoll = random.randint(1,6) #remember to knock 1 off when inputting for array
        #TODO: error handling for weaponRoll if any
        weaponSelected = weapons[weaponRoll - 1]
        print(f"Weapon Roll: {weaponRoll}. Weapon selected: {weaponSelected}")
        if weaponRoll <= 2:
            print("You rolled a weak weapon, friend")
        elif weaponRoll <= 4:
            print("Your weapon is meh.")
        else:
            print("Nice weapon, friend!")
        if weaponSelected != "Fist":
            print("Thank goodness you didn't roll a fist, eh?")
        else:
            print("...I'm sorry bud.")
    except:
        print("An error occured!")

if __name__ == "__main__":
    main()