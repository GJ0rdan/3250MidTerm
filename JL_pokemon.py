#Attempt at Pokemon class
import random

def chance():
    return random.choice([0, 1, 2, 3, 4])

class Pokemon:
    def __init__(self, name:str, hit:int, health:int):
        self.name = name
        self.hit = hit
        self.health = health
    def attack(self, Pokemon):
        attackChance = chance()
        if attackChance == 0:
            print(f"{self.name} ATTACKS!")
            print(f"{self.name}'s attack failed!")

        elif attackChance == 1 or 2 or 3:
            print(f"{self.name} ATTACKS!")
            print("Attack Successful!")
            Pokemon.health = Pokemon.health - self.hit

        else:
            print(f"{self.name} unleashes SUPER ATTACK!")
            print(f"{self.name}'s attack does DOUBLE DAMAGE!")
            Pokemon.health = Pokemon.health - 2*self.hit

        print(f"{self.name}'s health: "f"{self.health}")
        print(f"{Pokemon.name}'s health: "f"{Pokemon.health} \n")

    def defend(self):
        defensePerk = chance()
        if defensePerk == 0:
            print(f"{self.name} fails to Defend!")
        elif defensePerk == 1 or 2:
            print(f"{self.name} Enters Hibernation Mode! Health increases a little!")
            self.health = self.health + 100
        else:
            print(f"{self.name} Enters Meditative Mode! Health increases a significant amount!")
            self.health = self.health + 300

        print(f"{self.name}'s health: "f"{self.health} \n")

pikachu = Pokemon("Pikachu",100,1000)

snorlax = Pokemon("Snorlax",200,2000)

print("Select a Pokemon!")
p = input("""Pikachu or Snorlax: """)
p = str.lower(p)

if p == "pikachu":
    print("You chose "+ pikachu.name + "\n")
    p = pikachu.name
elif p == "snorlax":
    print("You chose "+ snorlax.name + "\n")
    p = snorlax.name
else:
    print("Not a Pokemon! Pikachu chosen as default\n")
    p = pikachu.name

if p == pikachu.name:
    print("Your opponent is " + snorlax.name + "!")
    print(pikachu.name + " begins with " + str(pikachu.health) + " and can attack with " + str(pikachu.hit) + " points.")
    print(snorlax.name + " begins with " + str(snorlax.health) + " and can attack with " + str(snorlax.hit) + " points.\n")
    print("Ready to begin?")
    tryAgain = input("Y/n: ") #Still need to complete loop to allow user to choose new Pokemon

    while pikachu.health > 0 and snorlax.health > 0:
        action = str.lower(input("Would you like to attack or defend?: "))
        if action == "attack":
            pikachu.attack(snorlax)
            retaliation = chance()
            if retaliation == 1 or 2 or 3:
                print(snorlax.name + " retaliates!")
                snorlax.attack(pikachu)
            
        if action == "defend":
            pikachu.defend()
            retaliation = chance()
            if retaliation == 0 or 4:
                print(pikachu.name + " was left vulnerable! \n" + snorlax.name + " decides to make a move!")
                snorlax.attack(pikachu)
# OPPONENT ACTIONS
        opponentActions = chance()
        if opponentActions == 0 or 1 or 2:
            print(snorlax.name + " chooses to attack!")
            snorlax.attack(pikachu)
            retaliation = chance()
            if retaliation == 1 or 2 or 3:
                print(pikachu.name + " retaliates!")
                pikachu.attack(snorlax)       
        else:
            print(snorlax.name + " chooses to defend!")
            snorlax.defend()
            retaliation = chance()
            if retaliation == 1 or 2 or 3:
                print(pikachu.name + " retaliates!")
                pikachu.attack(snorlax)


elif p == snorlax.name:
    print("Your opponent is " + pikachu.name + "!")
    print(snorlax.name + " begins with " + str(snorlax.health) + " and can attack with " + str(snorlax.hit) + " points.")
    print(pikachu.name + " begins with " + str(pikachu.health) + " and can attack with " + str(pikachu.hit) + " points.\n")
    print("Ready to begin?")
    tryAgain = input("Y/n: ") #Still need to complete loop to allow user to choose new Pokemon

    while pikachu.health > 0 and snorlax.health > 0:
        action = str.lower(input("Would you like to attack or defend?: "))
        if action == "attack":
            snorlax.attack(pikachu)
            retaliation = chance()
            if retaliation == 1 or 2 or 3:
                print(pikachu.name + " retaliates!")
                pikachu.attack(snorlax)
        if action == "defend":
            snorlax.defend()
            retaliation = chance()
            if retaliation == 2 or 3:
                pikachu.attack(snorlax)


if pikachu.health == 0:
    print(pikachu.name + " has lost! You need more training!")
    print(snorlax.name + " is VICTOR!")
elif snorlax.health == 0:
    print(snorlax.name + " has lost! You need more training!")
    print(pikachu.name + " is VICTOR!")

        

        
                
    


