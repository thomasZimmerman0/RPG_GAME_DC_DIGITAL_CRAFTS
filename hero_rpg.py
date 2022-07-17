
#todo Add dungeon scenario
#todo make cheesy story

import math
import random
import chara
import items
import time
import narrative

class Scenario:
    
    global_powder = items.Volatile_Powder(False)
    
    powder_dummy = False
    
    swap = False
    
    used_root = False
    
    root_stack = False
    
    equipped_weapon = []
    
    equipped_armor = []
    
    def fight(self, pc, npc):
        
        turn_counter = 0
        save_counter = 999
        save_counter0 = 999
        save_counter1 = 999
        save_counter2 = 999
        
        while pc.alive() and npc.alive():
            time.sleep(.5)
            
            pc.is_hero = True
            
            print(f'''
Your path collides with {npc.name}!
/////////////////////////////////////////
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
What is your next move?:
+=+=+=+=+=+=+=+=+=+=+=+=
1.   fight {npc.name}
2.     do nothing
3.     check bank
4.    check status
5.       flee
6.      use item
+=+=+=+=+=+=+=+=+=+=+=+=''')
            raw_input = input('>>')
            if raw_input == "1":
                pc.attack(npc)
                time.sleep(1.5)
                print()
                if self.global_powder.used == True:
                    print(f"{npc.name} stumbles and yells from the burning powder!")
                else:
                    npc.attack(pc)
                time.sleep(1.5)
                turn_counter += 1
            elif raw_input == "2":
                if self.global_powder.used == True:
                    print(f"{npc.name} stumbles and yells from the burning powder!")
                else:
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
            if self.global_powder.used == True and self.powder_dummy == True:
                save_counter1 = turn_counter
                self.powder_dummy = False
            
            if save_counter1 == turn_counter -2:
                self.global_powder.used = False
                save_counter1 = 999
                print(f"{npc.name} no longer burns from the powder!")
            #############################################################
            #######################
            if self.swap == True:
                save_counter0 = turn_counter
                self.swap = False
            
            if save_counter0 == turn_counter -1:
                scroll = items.Swap()
                scroll.bonus(npc, pc)
                save_counter0 = 999
                print('Your scroll of reversal has worn off!')
                
            ########################################################################################
            
            if self.used_root == True:
                save_counter = turn_counter
                self.used_root = False
                
            if save_counter == turn_counter - 3:
                root = items.Root()
                root.remove_root(pc)
                save_counter = 999
                print("Your strange root has worn off!")
                self.root_stack = False
            #####################################################################################
            if isinstance(npc, chara.Wizard):
                if npc.used_enchant == True:
                    save_counter2 = turn_counter
                    npc.used_enchant = False
            
            if save_counter2 == turn_counter -3:
                npc.power -= 4
                save_counter2 = 999
                print("The Wizard's enchantment dwindles to nothing!")    
            

#! Use item scenario prompts user to select an item to use in battle
    def use_item(self, pc, npc):
        
        super = items.SuperTonic()
        armor1 = items.Armorlv1()
        armor2 = items.Armorlv2()
        armor3 = items.Armorlv3()
        evade = items.Evade()
        root = items.Root()
        sword1 = items.Swordlv1()
        sword2 = items.Swordlv2()
        sword3 = items.Swordlv3()
        scroll = items.Swap()
        
        
        print('''
Which item would you like to use?
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+''') #Prints use item menu, takes into account you may have multiple of the same item
        dup = []
            
        for i in pc.item_list:
            if i not in dup:
                dup.append(i)
        for i in dup:
            if i == super.name:
                print(f"'Q'. {i} x{pc.itemQuant(i)}") #Calls a method in character class that returns the quantity of an item
            elif i == armor1.name:
                print(f"'W'. {i}")
            elif i == evade.name:
                print(f"'E'. {i} x{pc.itemQuant(i)}")
            elif i == root.name:
                print(f"'R'. {i} x{pc.itemQuant(i)}")
            elif i == sword1.name:
                print(f"'T'. {i}")
            elif i == scroll.name:
                print(f"'Y'. {i} x{pc.itemQuant(i)}")
            elif i == self.global_powder.name:
                print(f"'U'. {i} x{pc.itemQuant(i)}")
            elif i == armor2.name:
                print(f"'I'. {i} x{pc.itemQuant(i)}")
            elif i == armor3.name:
                print(f"'O'. {i} x{pc.itemQuant(i)}")
            elif i == sword2.name:
                print(f"'P'. {i} x{pc.itemQuant(i)}")
            elif i == sword3.name:
                print(f"'A'. {i} x{pc.itemQuant(i)}")
        print(f'1. Go back')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            
        option = input(">>").upper()
        
        if option == 'Q':
            
            super.use_item(pc, npc)
            
        elif option == 'W':
            #Every armor and weapon use item option has similar logic to deduce how the power level should be recaluculated. It's ugly, and redundant, but it works for the purpses of this project.
            if len(self.equipped_armor) == 0:
                armor1.use_item(pc, npc)
                self.equipped_armor.append(armor1.name)
                
            elif self.equipped_armor[0] == armor1.name:
                print ("Already Equipped!")
                
            elif self.equipped_armor[0] == armor2.name:
                armor2.remove(pc)
                self.equipped_armor.remove(armor2.name)
                armor1.use_item(pc, npc)
                self.equipped_armor.append(armor1.name)
                
            elif self.equipped_armor[0] == armor3.name:
                armor3.remove(pc)
                self.equipped_armor.remove(armor3.name)
                armor1.use_item(pc,npc)
                self.equipped_armor.append(armor1.name)

        elif option == 'E':
            
            evade.use_item(pc, npc)
            
        elif option == 'R':
            if self.root_stack == False: # global variable to ensure root isn't used more than once 
                print("Your muscles swell and your limbs feel weightless")
                
                root.use_item(pc,npc)
                self.used_root = True #Sets global variable used root to true in order to keep track of how many turns it lasts
                self.root_stack = True
            else:
                print("You can only take 1 strange root at a time!")
        
        elif option == 'T':
            #Every armor and weapon use item option has similar logic to deduce how the power level should be recaluculated. It's ugly, and redundant, but it works for the purpses of this project.
            if len(self.equipped_weapon) == 0:
                sword1.use_item(pc, npc)
                self.equipped_weapon.append(sword1.name)
                
            elif self.equipped_weapon[0] == sword2.name:
                sword2.remove(pc)
                self.equipped_weapon.remove(sword2.name)
                sword1.use_item(pc, npc)
                self.equipped_weapon.append(sword1.name)
                
            elif self.equipped_weapon[0] == sword3.name:
                sword3.remove(pc)
                self.equipped_weapon.remove(sword3.name)
                sword1.use_item(pc, npc)
                self.equipped_weapon.append(sword1.name)
                
            elif self.equipped_weapon[0] == sword1.name:
                print("Already Equipped!")
            
        
        elif option == 'Y':
            
            scroll.use_item(pc, npc)
            self.swap = True
        
        elif option == 'U':
            self.global_powder.use_item(pc, npc)
            self.powder_dummy = True
        
        elif option == 'I':
            
            if len(self.equipped_armor) == 0:
                armor2.use_item(pc, npc)
                self.equipped_armor.append(armor2.name)
                
            elif self.equipped_armor[0] == armor2.name:
                print ("Already Equipped!")
                
            elif self.equipped_armor[0] == armor3.name:
                armor3.remove(pc)
                self.equipped_armor.remove(armor3.name)
                armor2.use_item(pc, npc)
                self.equipped_armor.append(armor2.name)
                
            elif self.equipped_armor[0] == armor1.name:
                armor1.remove(pc)
                self.equipped_armor.remove(armor1.name)
                armor2.use_item(pc,npc)
                self.equipped_armor.append(armor2.name)

                
        elif option == 'O':
            
            if len(self.equipped_armor) == 0:
                armor3.use_item(pc, npc)
                self.equipped_armor.append(armor3.name)
                
            elif self.equipped_armor[0] == armor3.name:
                print ("Already Equipped!")
                
            elif self.equipped_armor[0] == armor2.name:
                armor2.remove(pc)
                self.equipped_armor.remove(armor2.name)
                armor3.use_item(pc, npc)
                self.equipped_armor.append(armor3.name)
                
            elif self.equipped_armor[0] == armor1.name:
                armor1.remove(pc)
                self.equipped_armor.remove(armor1.name)
                armor3.use_item(pc,npc)
                self.equipped_armor.append(armor3.name)

        
        elif option == 'P':
            
            if len(self.equipped_weapon) == 0:
                sword2.use_item(pc, npc)
                self.equipped_weapon.append(sword2.name)
                
            elif self.equipped_weapon[0] == sword2.name:
                print ("Already Equipped!")
                
            elif self.equipped_weapon[0] == sword3.name:
                sword3.remove(pc)
                self.equipped_weapon.remove(sword3.name)
                sword2.use_item(pc, npc)
                self.equipped_weapon.append(sword2.name)
                
            elif self.equipped_weapon[0] == sword1.name:
                sword1.remove(pc)
                self.equipped_weapon.remove(sword1.name)
                sword2.use_item(pc,npc)
                self.equipped_weapon.append(sword2.name)

                
        
        elif option == 'A':
            
            if len(self.equipped_weapon) == 0:
                sword3.use_item(pc, npc)
                self.equipped_weapon.append(sword3.name)
                
            elif self.equipped_weapon[0] == sword2.name:
                sword2.remove(pc)
                self.equipped_weapon.remove(sword2.name)
                sword3.use_item(pc, npc)
                self.equipped_weapon.append(sword3.name)
                
            elif self.equipped_weapon[0] == sword3.name:
                print ("Already Equipped!")
                
            elif self.equipped_weapon[0] == sword1.name:
                sword1.remove(pc)
                self.equipped_weapon.remove(sword1.name)
                sword3.use_item(pc,npc)
                self.equipped_weapon.append(sword3.name)


    #! Storefront scenario, allows player to buy items with that hard earned gold           
    def store(self, pc):
        
        supert = items.SuperTonic()
        armor1 = items.Armorlv1()
        evade = items.Evade()
        root = items.Root()
        swap = items.Swap()
        sword1 = items.Swordlv1()
        sword2 = items.Swordlv2()
        sword3 = items.Swordlv3()
        armor2 = items.Armorlv2()
        armor3 = items.Armorlv3()
        
        
        evade_stock = 5
        root_stock = 10
        Armor1_stock = 1
        dull_sabre_stock = 1
        
        while True:
            time.sleep(1)
            sale_txt = { 1:'Thanks for the gold!',
                         2:'If you get into trouble with that, you didn\'t get it from me',
                         3:'Come again soon!',
                         4:'I stopped asking questions a long time ago...'}
            print()
            print('''
Welcome to the general store:
+=+=+=+=+=+=+=+=+=+=+=+=+=+=++=+=+=+=+=+=+=+=+=+=+=+=+=+=+
1. SuperTonic       7 g     8. Used Chainmail Garb   40g

2. Old Leather Pads 15 g     9. Knight's Longsword    50g

3. Rune of Evasion  15 g    10. New Mastercrafted Knights
                                Suit of Armor         95g
4. Strange Root     6 g      

5. Dull Sabre       11 g    11.Arch Bishop Igor's Legendary
                               Diamond Encrusted Two-handed
6. Scroll of Reversal 8 g     Great Sword            110g

7. Hot bag of powder 8 g    0. Exit
+=+=+=+=+=+=+=+=+=+=+=+=+=+=++=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+''')
            option = input("What would you like to buy? >>")
            
            if option == '1' and pc.bank >= 7:
                pc.item_list.append(supert.name)
                pc.bank -= 7
                print(sale_txt[random.randrange(1,4)])
                print(f'you now have {pc.bank} gold')
            elif option == '2' and pc.bank >= 15:
                if Armor1_stock > 0:
                    pc.item_list.append(armor1.name)
                    pc.bank -= 10
                    print(sale_txt[random.randrange(1,4)])
                    print(f'you now have {pc.bank} gold')
                    Armor1_stock -= 1
                else:
                    print ("We won't have another one of those for a while...")
            elif option == '3' and pc.bank >= 15:
                if evade_stock > 0:
                    pc.item_list.append(evade.name)
                    pc.bank -= 15
                    print(sale_txt[random.randrange(1,4)])
                    print(f'you now have {pc.bank} gold')
                    evade_stock -= 1
                else:
                    print('You bought up our entire suppy!')
                    
            elif option == '4' and pc.bank >= 6:
                if root_stock > 0:
                    pc.item_list.append(root.name)
                    pc.bank -= 6 
                    print(sale_txt[random.randrange(1,4)])
                    print(f'you now have {pc.bank} gold')
                    root_stock -= 1
                else:
                    print('That\'s the last of my tree root')
                    
            elif option == '5' and pc.bank >= 11:
                if dull_sabre_stock > 0:
                    pc.item_list.append(sword1.name)
                    pc.bank -= 11
                    print(sale_txt[random.randrange(1,4)])
                    print(f'you now have {pc.bank} gold')
                    dull_sabre_stock -= 1
                else:
                    print('Come back next week if you really want another.')
                    
            elif option == '6' and pc.bank >= 8:
                pc.item_list.append(swap.name)
                pc.bank -= 8
                print(sale_txt[random.randrange(1,4)])
                print(f'you now have {pc.bank} gold')
                
            elif option == '7' and pc.bank >= 8:
                pc.item_list.append(self.global_powder.name)
                pc.bank -= 8
                print(sale_txt[random.randrange(1,4)])
                print(f'you now have {pc.bank} gold')
                
            elif option == '8' and pc.bank >= 40:
                pc.item_list.append(armor2.name)
                pc.bank -= 40
                print(sale_txt[random.randrange(1,4)])
                print(f'you now have {pc.bank} gold')
                
            elif option == '9' and pc.bank >= 50:
                pc.item_list.append(sword2.name)
                pc.bank -= 50
                print(sale_txt[random.randrange(1,4)])
                print(f'you now have {pc.bank} gold')
                
            elif option == '10' and pc.bank >= 95:
                pc.item_list.append(armor3.name)
                pc.bank -= 95
                print(sale_txt[random.randrange(1,4)])
                print(f'you now have {pc.bank} gold')
                
            elif option == '11' and pc.bank >= 110:
                pc.item_list.append(sword3.name)
                pc.bank -= 110
                print(sale_txt[random.randrange(1,4)])
                print(f'you now have {pc.bank} gold')
                
            elif option == '0':
                break
            
            else : 
                break
            
     
        
                
def main():
    
    text = narrative.Text()
    game = Scenario()
    # brawl = Scenario()
    # store = Scenario()
    
    # bro = chara.Hero()
    # giant = chara.Giant()
    # # goblin = chara.Goblin()
    # # zombie = chara.Zombie()
    # medic = chara.Medic()
    # shadow = chara.Shadow()
    # dweller = chara.Cave_Dweller()
    # dweller2 = chara.Cave_Dweller()
    # # gaurdsman = chara.Temple_Gaurd()
    # assass = chara.Assassian()
    # wizard = chara.Wizard()
    
    text.choose_character_menu()
    
    option = input("What is your choice? >>")
    
    if option == '1':
        hero = chara.Hero()
    elif option == '2':
        hero = chara.Medic() 
    elif option == '3':
        hero = chara.Assassian()
            
    text.OpeningTxt(hero)
    text.begin()
    
    option = input('''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
1. Go to the bar
2. Go to the General Store
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
>>''')
    if option == '1':
        pass
    elif option == '2':
        game.store(hero)
    
    
    
    
    
    
    
    
    
    
    
    
    # store.store(hero)
    # # # brawl.fight(hero, goblin)
    # # # brawl.fight(hero, medic)
    # # # brawl.fight(hero, shadow)
    # brawl.fight(hero, dweller)
    # # brawl.fight(hero, gaurdsman)
    # # brawl.fight(hero, dweller2)
    
   
    
    #store.store(hero)
    
main()

