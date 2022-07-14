# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

#todo Add character select scenario

import math
import random
import rpg_game.Character as Character

class Scenario:
    
    def fight(self, pc, npc):
        while pc.alive() and npc.alive():
            print()
            print("What do you want to do?")
            print(f"1. fight {npc.name}")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                pc.attack(npc)
                npc.attack(pc)
                npc.print_status()
                pc.print_status()
            elif raw_input == "2":
                npc.attack(pc)
                pc.print_status()
                npc.print_status()
            elif raw_input == "3":
                print("Goodbye.")
                break
            else:
                print(f"Invalid input {raw_input}")
        
    
class Hero(Character):
    
    is_hero = True
    
    def __init__(self):
        super().__init__('Hero', 100, 5)

    def critical(self):
        self.power += self.power
    
class Goblin(Character):
    
    is_hero = False
    
    def __init__(self):
        super().__init__('the goblin', 6, 3)

class Zombie(Character):
    
    is_hero = False
    
    def __init__(self):
        super().__init__('the zombie', math.inf, 4 )

class Medic(Character):
    
    is_hero = False
    
    def __init__(self):
        super().__init__('Medic', 30, 3)
        
    def heal(self):
        self.health += 2

class Shadow(Character):
    
    is_hero = False
    
    def __init__(self):
        super().__init__('Shadow', 1, 5)
 

         
                
def main():

    brawl = Scenario()
    
    
    hero = Hero()
    goblin = Goblin()
    zombie = Zombie()
    medic = Medic()
    shadow = Shadow()

    brawl.fight(hero, goblin)
    brawl.fight(hero, zombie)
    brawl.fight(hero, medic)
    brawl.fight(hero, shadow)
    
    brawl.fight(medic, shadow)
    
main()

