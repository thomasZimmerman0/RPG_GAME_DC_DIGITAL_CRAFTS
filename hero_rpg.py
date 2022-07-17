
#todo make cheesy story (wip)

import math
import random
import chara
import items
import time
import narrative

class Scenario:
    #? Variables made to use item objects within the Scenario class
    
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
    
    #? Variables made in order to keep items fully functional, keep track of turns and equipted
    #? weapons and armor/
    global_powder = items.Volatile_Powder(False)
    
    powder_dummy = False
    
    swap = False
    
    used_root = False
    
    root_stack = False
    
    equipped_weapon = []
    
    equipped_armor = []

#! Primary function of this entire game lol  
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
Your might collides with that of {npc.name}!
/////////////////////////////////////////////
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
What is your next move?:
+=+=+=+=+=+=+=+=+=+=+=+=+
) 1.  fight {npc.name}  
) 2.     do nothing     
) 3.  study {npc.name}  
) 4.      status        
) 5.       flee         
) 6.     use item       
+=+=+=+=+=+=+=+=+=+=+=+=+''')
            raw_input = input('>>')
            if raw_input == "1":
                pc.attack(npc)
                time.sleep(1.5)
                print()
                if self.global_powder.used == True and npc.alive():
                    print(f"{npc.name} stumbles and yells from the burning powder!")
                else:
                    npc.attack(pc)
                time.sleep(1.5)
                turn_counter += 1
                
            elif raw_input == "2":
                if self.global_powder.used == True and npc.alive():
                    print(f"{npc.name} stumbles and yells from the burning powder!")
                else:
                    npc.attack(pc)
                turn_counter += 1
                
            elif raw_input == "3":
                npc.print_status()
                time.sleep(2)
                if self.global_powder.used == True and npc.alive():
                    print(f"{npc.name} stumbles and yells from the burning powder!")
                else:
                    npc.attack(pc)
                turn_counter += 1
                
            elif raw_input == "4":
                pc.print_status()
                
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
            
            if save_counter1 == turn_counter -2 or (save_counter1 < turn_counter and npc.alive() == False):
                self.global_powder.used = False
                save_counter1 = 999
                if save_counter1 < turn_counter and npc.alive() == True:
                    print(f"{npc.name} no longer burns from the powder!")
                    
            ####################################################################################
            if self.swap == True:
                save_counter0 = turn_counter
                self.swap = False
            
            if save_counter0 == turn_counter -1 or (save_counter0 < turn_counter and npc.alive() == False):
                self.scroll.bonus(npc, pc)
                save_counter0 = 999
                print('Your scroll of reversal has worn off!')
                
            ########################################################################################
            
            if self.used_root == True:
                save_counter = turn_counter
                self.used_root = False
                
            if save_counter == turn_counter - 3 or (save_counter < turn_counter and npc.alive() == False):
                self.root.remove_root(pc)
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
        

        
        
        print('''
Which item would you like to use?
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+''') #Prints use item menu, takes into account you may have multiple of the same item
        dup = []
            
        for i in pc.item_list:
            if i not in dup:
                dup.append(i)
        for i in dup:
            if i == self.super.name:
                print(f"'Q'. {i} x{pc.itemQuant(i)}") #Calls a method in character class that returns the quantity of an item
            elif i == self.armor1.name:
                print(f"'W'. {i}")
            elif i == self.evade.name:
                print(f"'E'. {i} x{pc.itemQuant(i)}")
            elif i == self.root.name:
                print(f"'R'. {i} x{pc.itemQuant(i)}")
            elif i == self.sword1.name:
                print(f"'T'. {i}")
            elif i == self.scroll.name:
                print(f"'Y'. {i} x{pc.itemQuant(i)}")
            elif i == self.global_powder.name:
                print(f"'U'. {i} x{pc.itemQuant(i)}")
            elif i == self.armor2.name:
                print(f"'I'. {i} x{pc.itemQuant(i)}")
            elif i == self.armor3.name:
                print(f"'O'. {i} x{pc.itemQuant(i)}")
            elif i == self.sword2.name:
                print(f"'P'. {i} x{pc.itemQuant(i)}")
            elif i == self.sword3.name:
                print(f"'A'. {i} x{pc.itemQuant(i)}")
        print(f'1. Go back')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            
        option = input(">>").upper()
        
        if option == 'Q':
            
            self.super.use_item(pc, npc)
            
        elif option == 'W':
            #Every armor and weapon use item option has similar logic to deduce how the power level should be recaluculated. It's ugly, and redundant, but it works for the purpses of this project.
            if len(self.equipped_armor) == 0:
                self.armor1.use_item(pc, npc)
                self.equipped_armor.append(self.armor1.name)
                
            elif self.equipped_armor[0] == self.armor1.name:
                print ("Already Equipped!")
                
            elif self.equipped_armor[0] == self.armor2.name:
                self.armor2.remove(pc)
                self.equipped_armor.remove(self.armor2.name)
                self.armor1.use_item(pc, npc)
                self.equipped_armor.append(self.armor1.name)
                
            elif self.equipped_armor[0] == self.armor3.name:
                self.armor3.remove(pc)
                self.equipped_armor.remove(self.armor3.name)
                self.armor1.use_item(pc,npc)
                self.equipped_armor.append(self.armor1.name)

        elif option == 'E':
            
            self.evade.use_item(pc, npc)
            
        elif option == 'R':
            if self.root_stack == False: # global variable to ensure root isn't used more than once 
                print("Your muscles swell and your limbs feel weightless")
                
                self.root.use_item(pc,npc)
                self.used_root = True #Sets global variable used root to true in order to keep track of how many turns it lasts
                self.root_stack = True
            else:
                print("You can only take 1 strange root at a time!")
        
        elif option == 'T':
            #Every armor and weapon use item option has similar logic to deduce how the power level should be recaluculated. It's ugly, and redundant, but it works for the purpses of this project.
            if len(self.equipped_weapon) == 0:
                self.sword1.use_item(pc, npc)
                self.equipped_weapon.append(self.sword1.name)
                
            elif self.equipped_weapon[0] == self.sword2.name:
                self.sword2.remove(pc)
                self.equipped_weapon.remove(self.sword2.name)
                self.sword1.use_item(pc, npc)
                self.equipped_weapon.append(self.sword1.name)
                
            elif self.equipped_weapon[0] == self.sword3.name:
                self.sword3.remove(pc)
                self.equipped_weapon.remove(self.sword3.name)
                self.sword1.use_item(pc, npc)
                self.equipped_weapon.append(self.sword1.name)
                
            elif self.equipped_weapon[0] == self.sword1.name:
                print("Already Equipped!")
            
        
        elif option == 'Y':
            
            self.scroll.use_item(pc, npc)
            self.swap = True
        
        elif option == 'U':
            self.global_powder.use_item(pc, npc)
            self.powder_dummy = True
        
        elif option == 'I':
            
            if len(self.equipped_armor) == 0:
                self.armor2.use_item(pc, npc)
                self.equipped_armor.append(self.armor2.name)
                
            elif self.equipped_armor[0] == self.armor2.name:
                print ("Already Equipped!")
                
            elif self.equipped_armor[0] == self.armor3.name:
                self.armor3.remove(pc)
                self.equipped_armor.remove(self.armor3.name)
                self.armor2.use_item(pc, npc)
                self.equipped_armor.append(self.armor2.name)
                
            elif self.equipped_armor[0] == self.armor1.name:
                self.armor1.remove(pc)
                self.equipped_armor.remove(self.armor1.name)
                self.armor2.use_item(pc,npc)
                self.equipped_armor.append(self.armor2.name)

                
        elif option == 'O':
            
            if len(self.equipped_armor) == 0:
                self.armor3.use_item(pc, npc)
                self.equipped_armor.append(self.armor3.name)
                
            elif self.equipped_armor[0] == self.armor3.name:
                print ("Already Equipped!")
                
            elif self.equipped_armor[0] == self.armor2.name:
                self.armor2.remove(pc)
                self.equipped_armor.remove(self.armor2.name)
                self.armor3.use_item(pc, npc)
                self.equipped_armor.append(self.armor3.name)
                
            elif self.equipped_armor[0] == self.armor1.name:
                self.armor1.remove(pc)
                self.equipped_armor.remove(self.armor1.name)
                self.armor3.use_item(pc,npc)
                self.equipped_armor.append(self.armor3.name)

        
        elif option == 'P':
            
            if len(self.equipped_weapon) == 0:
                self.sword2.use_item(pc, npc)
                self.equipped_weapon.append(self.sword2.name)
                
            elif self.equipped_weapon[0] == self.sword2.name:
                print ("Already Equipped!")
                
            elif self.equipped_weapon[0] == self.sword3.name:
                self.sword3.remove(pc)
                self.equipped_weapon.remove(self.sword3.name)
                self.sword2.use_item(pc, npc)
                self.equipped_weapon.append(self.sword2.name)
                
            elif self.equipped_weapon[0] == self.sword1.name:
                self.sword1.remove(pc)
                self.equipped_weapon.remove(self.sword1.name)
                self.sword2.use_item(pc,npc)
                self.equipped_weapon.append(self.sword2.name)

                
        
        elif option == 'A':
            
            if len(self.equipped_weapon) == 0:
                self.sword3.use_item(pc, npc)
                self.equipped_weapon.append(self.sword3.name)
                
            elif self.equipped_weapon[0] == self.sword2.name:
                self.sword2.remove(pc)
                self.equipped_weapon.remove(self.sword2.name)
                self.sword3.use_item(pc, npc)
                self.equipped_weapon.append(self.sword3.name)
                
            elif self.equipped_weapon[0] == self.sword3.name:
                print ("Already Equipped!")
                
            elif self.equipped_weapon[0] == self.sword1.name:
                self.sword1.remove(pc)
                self.equipped_weapon.remove(self.sword1.name)
                self.sword3.use_item(pc,npc)
                self.equipped_weapon.append(self.sword3.name)


    #! Storefront scenario, allows player to buy items with that hard earned gold           
    def store(self, pc):
        
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
                pc.item_list.append(self.super.name)
                pc.bank -= 7
                print(sale_txt[random.randrange(1,5)])
                print(f'you now have {pc.bank} gold')
            elif option == '2' and pc.bank >= 15:
                if Armor1_stock > 0:
                    pc.item_list.append(self.armor1.name)
                    pc.bank -= 10
                    print(sale_txt[random.randrange(1,5)])
                    print(f'you now have {pc.bank} gold')
                    Armor1_stock -= 1
                else:
                    print ("We won't have another one of those for a while...")
            elif option == '3' and pc.bank >= 15:
                if evade_stock > 0:
                    pc.item_list.append(self.evade.name)
                    pc.bank -= 15
                    print(sale_txt[random.randrange(1,5)])
                    print(f'you now have {pc.bank} gold')
                    evade_stock -= 1
                else:
                    print('You bought up our entire suppy!')
                    
            elif option == '4' and pc.bank >= 6:
                if root_stock > 0:
                    pc.item_list.append(self.root.name)
                    pc.bank -= 6 
                    print(sale_txt[random.randrange(1,5)])
                    print(f'you now have {pc.bank} gold')
                    root_stock -= 1
                else:
                    print('That\'s the last of my tree root')
                    
            elif option == '5' and pc.bank >= 11:
                if dull_sabre_stock > 0:
                    pc.item_list.append(self.sword1.name)
                    pc.bank -= 11
                    print(sale_txt[random.randrange(1,5)])
                    print(f'you now have {pc.bank} gold')
                    dull_sabre_stock -= 1
                else:
                    print('Come back next week if you really want another.')
                    
            elif option == '6' and pc.bank >= 8:
                pc.item_list.append(self.swap.name)
                pc.bank -= 8
                print(sale_txt[random.randrange(1,5)])
                print(f'you now have {pc.bank} gold')
                
            elif option == '7' and pc.bank >= 8:
                pc.item_list.append(self.global_powder.name)
                pc.bank -= 8
                print(sale_txt[random.randrange(1,5)])
                print(f'you now have {pc.bank} gold')
                
            elif option == '8' and pc.bank >= 40:
                pc.item_list.append(self.armor2.name)
                pc.bank -= 40
                print(sale_txt[random.randrange(1,5)])
                print(f'you now have {pc.bank} gold')
                
            elif option == '9' and pc.bank >= 50:
                pc.item_list.append(self.sword2.name)
                pc.bank -= 50
                print(sale_txt[random.randrange(1,5)])
                print(f'you now have {pc.bank} gold')
                
            elif option == '10' and pc.bank >= 95:
                pc.item_list.append(self.armor3.name)
                pc.bank -= 95
                print(sale_txt[random.randrange(1,5)])
                print(f'you now have {pc.bank} gold')
                
            elif option == '11' and pc.bank >= 110:
                pc.item_list.append(self.sword3.name)
                pc.bank -= 110
                print(sale_txt[random.randrange(1,5)])
                print(f'you now have {pc.bank} gold')
                
            elif option == '0':
                break
            
            else : 
                break
    
    def Bullingham(self, game, text, hero):
        while True:
            text.Bullingham()
            option = input('>>')
            if option == '1':
                text.General_Store()
                game.store(hero)
            elif option == '2': 
                text.Deep_Woods_0()
                break
            
    def DeepWoods(self, game, text, hero):
        text.Deep_Woods_1()
        option = input('>>')
        if option == '1':
            text.abandoned_cart()
            game.Fight_Dweller(game, hero)
            text.abandoned_cart_win()
            print()
            hero.item_list.append(self.sword1.name)
            hero.item_list.append(self.super.name)
            print(f"You acquired a {self.sword1.name}!")
            print(f"You acquired a {self.super.name}!")
            game.Fight_Dweller(game, hero)
            
        elif option == '2':
            pass
        
    def GoblinSpree(self, game, hero):
        deepwoodsGoblin0 = chara.Goblin()
        deepwoodsGoblin1 = chara.Goblin()
        deepwoodsGoblin2 = chara.Goblin()
        deepwoodsGoblin0.hold_values()
        deepwoodsGoblin1.hold_values()
        deepwoodsGoblin2.hold_values()
        
        game.fight(hero, deepwoodsGoblin0)
        game.fight(hero, deepwoodsGoblin1)
        game.fight(hero, deepwoodsGoblin2)

        deepwoodsGoblin0.reset()
        deepwoodsGoblin1.reset()
        deepwoodsGoblin2.reset()
    
    def Fight_Dweller(self, game, hero):
        caveDweller = chara.Cave_Dweller()
        caveDweller.hold_values()
        
        game.fight(hero, caveDweller)

        caveDweller.reset()
        
        
            
        
            
def main():     
    
    text = narrative.Text()
    game = Scenario()

    text.choose_character_menu()

    option = input("What is your choice? >>")

    if option == '1':
        hero = chara.Hero()
    elif option == '2':
        hero = chara.Medic() 
    elif option == '3':
        hero = chara.Assassian()
            
    text.Backstory(hero)
    text.begin()
    
    while True:
        
        text.choice_0()

        option = input('>>')
        
        if option == '1':
            text.Tavern(hero)
            break
        elif option == '2':
            text.General_Store()
            game.store(hero)


    game.Bullingham(game, text, hero)
    
    game.GoblinSpree(game, hero)
    
    game.DeepWoods(game, text, hero)

    

    
main()












