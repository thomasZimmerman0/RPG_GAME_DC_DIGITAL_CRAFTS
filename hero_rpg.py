
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
    
    swap = False
    
    used_root = False
    
    root_stack = False
    
    def fight(self, pc, npc):
        
        turn_counter = 0
        save_counter = 999
        save_counter0 = 999
        
        while pc.alive() and npc.alive():
            time.sleep(.5)
            
            pc.is_hero = True
            
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
6. use item''')
            raw_input = input('>>')
            if raw_input == "1":
                pc.attack(npc)
                time.sleep(1.5)
                print()
                npc.attack(pc)
                time.sleep(1.5)
                turn_counter += 1
            elif raw_input == "2":
                npc.attack(pc)
                turn_counter += 1
            elif raw_input == "3":
                print(f"{pc.bank}")
            elif raw_input == "4":
                pc.print_status()
                npc.print_status()
            elif raw_input == '5':
                print("Goodbye!")
                break
            elif raw_input == '6':
                self.use_item(pc, npc)
            else:
                print(f"Invalid input {raw_input}")
            
            #? Everything below this comment in this method is logic dedicated to making turn based 
            #? items function the way they are supposed to
            
            if self.swap == True:
                save_counter0 = turn_counter
                self.swap = False
            
            if save_counter0 == turn_counter -1:
                scroll = items.Items('Scroll of Reversal')
                scroll.Swap(npc, pc)
                print('Your scroll of reversal has worn off!')
                
            ########################################################################################
            
            if self.used_root == True:
                save_counter = turn_counter
                self.used_root = False
                
            if save_counter == turn_counter - 3:
                root = items.Items('Root of the Mutant Tree')
                root.Remove_Root(pc)
                save_counter = 999
                print("Your strange root has worn off!")
                self.root_stack = False

#! Use item scenario prompts user to select an item to use in battle
    def use_item(self, pc, npc):
        
        
        
        print('''
Which item would you like to use?
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+''') #Prints use item menu, takes into account you may have multiple of the same item
        dup = []
            
        for i in pc.item_list:
            if i not in dup:
                dup.append(i)
        for i in dup:
            if i == 'SuperTonic':
                print(f"'Q'. {i} x{pc.itemQuant(i)}") #Calls a method in character class that returns the quantity of an item
            elif i == 'Old Leather Pads':
                print(f"'W'. {i}")
            elif i == 'Rune of Evasion':
                print(f"'E'. {i} x{pc.itemQuant(i)}")
            elif i == 'Root of the Mutant Tree':
                print(f"'R'. {i} x{pc.itemQuant(i)}")
            elif i == 'Dull Sabre':
                print(f"'T'. {i}")
            elif i == 'Scroll of Reversal':
                print(f"'Y'. {i} x{pc.itemQuant(i)}")
        print(f'1. Go back')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            
        option = input(">>").upper()
        if option == 'Q':
            super = items.Items('SuperTonic')
            super.SuperTonic(pc)
            
        elif option == 'W':
            armor = items.Items('Old Leather Pads')
            armor.Armor(pc)

        elif option == 'E':
            evade = items.Items('Rune of Evasion')
            evade.Evade(pc)
            
        elif option == 'R':
            if self.root_stack == False: # global variable to ensure root isn't used more than once 
                print("Your muscles swell and your limbs feel weightless")
                root = items.Items('Root of the Mutant Tree')
                root.Root(pc)
                self.used_root = True #Sets global variable used root to true in order to keep track of how many turns it lasts
                self.root_stack = True
            else:
                print("You can only take 1 strange root at a time!")
        
        elif option == 'T':
            sabre = items.Items('Dull Sabre')
            sabre.Dull_Sabre(pc)
        
        elif option == 'Y':
            scroll = items.Items('Scroll of Reversal')
            scroll.Swap(pc, npc)
            self.swap = True
            
        elif option == '1':
            pass

    #! Storefront scenario, allows player to buy items with that hard earned gold           
    def store(self, pc):
        
        evade_stock = 4
        root_stock = 10
        Armor1_stock = 1
        dull_sabre_stock = 1
        
        while True:
            sale_txt = { 1:'Thanks for the gold!',
                         2:'If you get into trouble with that, you didn\'t get it from me',
                         3:'Come again soon!',
                         4:'I stopped asking questions a long time ago...'}
            print()
            print('''
Welcome to the general store:
+=+=+=+=+=+=+=+=+=+=+=+=+=+=++=+=+=+=+=+=+=+=+=+=+=+=+=+=+
1. SuperTonic       10 gold 
2. Old Leather Pads 10 gold
3. Rune of Evasion  10 gold
4. Strange Root     10 gold
5. Dull Sabre       10 gold 
6. Scroll of Reversal  10 gold 
+=+=+=+=+=+=+=+=+=+=+=+=+=+=++=+=+=+=+=+=+=+=+=+=+=+=+=+=+''')
            option = int(input("What would you like to buy? >>"))
            
            if option == 1 and pc.bank >= 10:
                pc.item_list.append('SuperTonic')
                pc.bank -= 10
                print(sale_txt[1])
                print(pc.bank)
            elif option == 2 and pc.bank >=10:
                if Armor1_stock > 0:
                    pc.item_list.append('Old Leather Pads')
                    pc.bank -= 10
                    print(sale_txt[1])
                    print(pc.bank)
                    Armor1_stock -= 1
                else:
                    print ("We won't have another one of those for a while...")
            elif option == 3 and pc.bank >= 10:
                if evade_stock > 0:
                    pc.item_list.append('Rune of Evasion')
                    pc.bank -= 10
                    print(sale_txt[2])
                    print(pc.bank)
                    evade_stock -= 1
                else:
                    print('You bought up our entire suppy!')
                    
            elif option == 4 and pc.bank >= 10:
                if root_stock > 0:
                    pc.item_list.append('Root of the Mutant Tree')
                    pc.bank -= 10 
                    print(sale_txt[4])
                    print(pc.bank)
                    root_stock -= 1
                else:
                    print('That\'s the last of my tree root')
            elif option == 5 and pc.bank >= 10:
                if dull_sabre_stock > 0:
                    pc.item_list.append('Dull Sabre')
                    pc.bank -= 10
                    print(sale_txt[3])
                    print(pc.bank)
                    dull_sabre_stock -= 1
                else:
                    print('Come back next week if you really want another.')
            elif option == 6 and pc.bank >= 10:
                pc.item_list.append('Scroll of Reversal')
                pc.bank -= 10
                print(sale_txt[1])
                print (pc.bank)
            else :
                break
            
            
        
                
def main():

    brawl = Scenario()
    store = Scenario()
    
    
    hero = chara.Hero()
    # goblin = chara.Goblin()
    # zombie = chara.Zombie()
    medic = chara.Medic()
    shadow = chara.Shadow()
    dweller = chara.Cave_Dweller()
    dweller2 = chara.Cave_Dweller()
    # gaurdsman = chara.Temple_Gaurd()
    
    store.store(dweller2)
    # # brawl.fight(hero, goblin)
    # # brawl.fight(hero, medic)
    # # brawl.fight(hero, shadow)
    brawl.fight(shadow, dweller2)
    # brawl.fight(hero, gaurdsman)
    # brawl.fight(hero, dweller2)
    
   
    
    #store.store(hero)
    
    #? Reference to a call on an item >>
    #? superTonic = items.Items('SuperTonic', 'Health')
    #? superTonic.SuperTonic(pc)
main()

