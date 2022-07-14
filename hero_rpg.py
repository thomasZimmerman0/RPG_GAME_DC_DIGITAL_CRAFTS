# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

#todo Add character select scenario
#lol


import math
import random
import chara

class Scenario:
    
    def fight(self, pc, npc):
        while pc.alive() and npc.alive():
            print()
            print("What do you want to do?")
            print(f"1. fight {npc.name}")
            print("2. do nothing")
            print("3. check bank")
            print("4. Check status")
            print("5. flee")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                pc.attack(npc)
                npc.attack(pc)
            elif raw_input == "2":
                npc.attack(pc)
            elif raw_input == "3":
                print(f"{pc.bank}")
            elif raw_input == "4":
                pc.print_status()
                npc.print_status()
            elif raw_input == '5':
                print("Goodbye!")
                break
            else:
                print(f"Invalid input {raw_input}")
        
                
def main():

    brawl = Scenario()
    
    
    hero = chara.Hero()
    goblin = chara.Goblin()
    zombie = chara.Zombie()
    medic = chara.Medic()
    shadow = chara.Shadow()
    dweller = chara.Cave_Dweller()
    dweller2 = chara.Cave_Dweller()
    gaurdsman = chara.Temple_Gaurd()
    # brawl.fight(hero, goblin)
    # brawl.fight(hero, medic)
    # brawl.fight(hero, shadow)
    brawl.fight(hero, dweller)
    brawl.fight(hero, gaurdsman)
    brawl.fight(hero, dweller2)
    
main()

