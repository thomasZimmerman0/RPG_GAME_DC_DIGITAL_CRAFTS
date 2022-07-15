
#todo Add character select scenario
#todo Add dungeon scenario
#todo make cheesy story
#todo make items menu and items class

import math
import random
import chara
import items
import time

class Scenario:
    
    used_root = False
    
    def fight(self, pc, npc):
        
        turn_counter = 0
        save_counter = 0
        
        while pc.alive() and npc.alive():
            print(f'''
Your path collides with {npc.name}!
////////////////////////
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
What is your next move?:
1. fight {npc.name}
2. do nothing
3. check bank
4. check status
5. flee
6. use item
>>''')
            raw_input = input()
            if raw_input == "1":
                pc.attack(npc)
                time.sleep(1.5)
                print()
                npc.attack(pc)
                time.sleep(1.5)
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
            elif raw_input == '6':
                self.use_item(pc)
            else:
                print(f"Invalid input {raw_input}")
            
            
            turn_counter += 1
            
            if self.used_root == True:
                save_counter = turn_counter
                self.used_root = False
            
            if save_counter == turn_counter - 2:
                root = items.Items('Root of the Mutant Tree')
                root.Remove_Root(pc)

#! Use item scenario prompts user to select an item to use in battle
    def use_item(self, pc):
        
        print('''
Which item would you like to use?
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+''') #Prints use item menu, takes into account you may have multiple of the same item
        count = 1
        dup = []
            
        for i in pc.item_list:
            if i not in dup:
                dup.append(i)
                print(f"{count}. {i} x{pc.itemQuant(i)}") #Calls a method in character class that returns the quantity of an item
                count += 1
        print(f'{count} Go back')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            
        option = int(input(">>"))
        if option == 1:
            super = items.Items('SuperTonic')
            super.SuperTonic(pc)
            print(f'{pc.health}')
        elif option == 2:
            armor = items.Items('Armor')
            armor.Armor(pc)
            print(f'{pc.armor_rating}')
        elif option == 3:
            evade = items.Items('Evade')
            evade.Evade(pc)
            print(f'{pc.evade}')
        elif option == 4:
            root = items.Items('Root of the Mutant Tree')
            root.Root(pc)
            print(f'{pc.power}')
            self.used_root = True #Sets global variable used root to true in order to keep track of how many turns it lasts

                
    def store(self, pc):
        while True:
            sale_txt = { 1:'Thanks for the gold!',
                         2:'If you get into trouble with that, you didn\'t get it from me',
                         3:'Come again soon!',
                         4:'I stopped asking questions a long time ago...'}
            print()
            print('''
Welcome to the general store:
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
1. SuperTonic 10 gold
2. Armor      10 gold
3. Evade      10 gold
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+''')
            option = int(input("What would you like to buy? >>"))
            
            if option == 1 and pc.bank >= 10:
                pc.item_list.append('SuperTonic')
                pc.bank -= 10
                print(sale_txt[1])
                print(pc.bank)
            elif option == 2 and pc.bank >=10:
                pc.item_list.append('Armor')
                pc.bank -= 10
                print(sale_txt[1])
                print(pc.bank)
            elif option == 3 and pc.bank >= 10:
                pc.item_list.append('Evade')
                pc.bank -= 10
                print(sale_txt[2])
                print(pc.bank)
            else :
                break
            
            
        
                
def main():

    brawl = Scenario()
    store = Scenario()
    
    
    hero = chara.Hero()
    # goblin = chara.Goblin()
    # zombie = chara.Zombie()
    # medic = chara.Medic()
    # shadow = chara.Shadow()
    dweller = chara.Cave_Dweller()
    # dweller2 = chara.Cave_Dweller()
    # gaurdsman = chara.Temple_Gaurd()
    
    store.store(hero)
    # # brawl.fight(hero, goblin)
    # # brawl.fight(hero, medic)
    # # brawl.fight(hero, shadow)
    brawl.fight(hero, dweller)
    # brawl.fight(hero, gaurdsman)
    # brawl.fight(hero, dweller2)
    
   
    
    #store.store(hero)
    
    #? Reference to a call on an item >>
    #? superTonic = items.Items('SuperTonic', 'Health')
    #? superTonic.SuperTonic(pc)
main()

