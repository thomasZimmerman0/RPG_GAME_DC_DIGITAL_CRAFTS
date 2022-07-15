import random
import math

class Character:
    
    
    chance_success = False
    
    dam_ref = 0
    
    bank = 9999
    
    item_list = []
    
    def __init__(self, name, health, power, armor_rating, evade):
        self.name = name
        self.health = health
        self.power = power
        self.armor_rating = armor_rating
        self.evade = evade
        

        
    
    #! Checks to see if the character is still alive
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
        
    #! Prints health and power of the character
    def print_status(self):
        if self.is_hero == True:
            print(f"Health:  {self.health}\nDamage:  {self.power}\nArmor:  {self.armor_rating}\nEvasion: {self.evade} ")
        elif self.is_hero == False:
            print(f"{self.name} has {self.health} health and {self.power} power.")
    
    ##################################################################################################################
    ##################################################################################################################
    #! Takes in 2 characters and performs multiple calculations and prints accordingly 
    #? Character based calculations are performed and checked within this method
    def attack(self, defense):
        
        
        orig_power = self.power #holds original value for power for player and npc's
        
        
        self.rng(20)#calls for a 20% chance of success for hero's (the player's) critical hit
        if self.chance_success == True and isinstance(self, Hero): #Will currently only work on Hero character
            print("Critical hit!")
            self.critical() #Temporarily double's hero's damage if successful
        
        if isinstance(defense, Shadow): 
            defense.rng(10)
            if defense.chance_success == False:
                self.power = 0
        
        if isinstance(self, Cave_Dweller):
            self.rng(20)
            if self.chance_success == True:
                print(f"{self.name} went berzerk!")
                self.berzerk()
                
        if isinstance(self, Temple_Gaurd):
            self.rng(50)
            if self.chance_success == True:
                print(f"Gaurdsman striked with force!")
                self.heavy()
        
        #! Health diminishment calculation! All damage mutlipliers should be done before this block!
        #!#########################################################################################
        if self.evade > 4: #Ensures evasion can not exceed 20%
            self.evade == 4
            
        self.rng(defense.evade * 5) #Calculates defense's evasion score for a chance to miss the attack
        if self.chance_success == True:
            if self.is_hero == True:
                print(f"{defense.name} slipped your attack!")
            elif self.is_hero == False:
                print(f"You evaded {self.name}'s attack!")
            self.chance_success = False
            self.dam_ref = 0
        else: # When evasion is unsuccessful, simmply calculate damage done
            defense.health = defense.health - (self.power - defense.armor_rating)
            self.dam_ref = (self.power - defense.armor_rating)
        #!#########################################################################################
        #!#########################################################################################
        
        if self.is_hero == True: #Runs if it is the player character attacking
            print(f"You do {self.dam_ref} damage to {defense.name}.")
            self.power = orig_power #Resets multiplier if it was successful
            
            
            if isinstance(defense, Medic):                #Performs Medics special ability 
                defense.rng(20)                           #for a chance to heal after being 
                if defense.chance_success == True and defense.alive():        #attacked by the player
                    defense.health += 2
                    print(f"{defense.name} healed!")
                    
                
        elif self.is_hero == False and self.alive(): #Runs when npc attacks player character
            print(f"{self.name} does {self.dam_ref} damage to you.")
            if isinstance(self, Cave_Dweller):
                self.power = orig_power #Resets cave dweller ability bonus.
            if isinstance(self, Temple_Gaurd):
                self.power = orig_power #resets gaurdsman ability bonus
            if defense.alive() == False:
                print("You are dead.")
                
        if self.is_hero == False and defense.alive() == False: #This if block will contain if statemtns pertaining to unique drops
            print(f"{defense.name} is dead.")
            print(f"You got {self.bounty(defense)} gold!")
            if isinstance(defense, Medic): #Checks if the enemy type was Medic, prints Medic's special drop
                print(f"The medic dropped 1 SuperTonic!") 
            
            
    ##################################################################################################################
    ##################################################################################################################
    #! Random number generator used to determine if a probability based attack / defense will succeed
    def rng(self, chance):
        number = random.randrange(1, 100)
        if number <= chance:
            self.chance_success = True
        else: 
            self.chance_success = False
    
    #! Calculates the players reward for each kill
    def bounty(self, type):
        
        reward = 0
        
        if isinstance(type, Goblin):
            reward = 5
        elif isinstance(type, Medic ):
            reward = 7
            self.item_list.append('SuperTonic')
        elif isinstance(type, Shadow):
            reward = 20
        elif isinstance(type, Cave_Dweller):
            reward = 8
        elif isinstance(type, Temple_Gaurd):
            reward = 14
            
        self.bank += reward
        
        return reward

    #! Returns quantity of a specific item 
    def itemQuant (self, item):
        
        quantity = 0
        
        for i in self.item_list:
            if i == item:
                quantity += 1
        return quantity
            
    
##################################################################################################################
##################################################################################################################
    
class Hero(Character):
    
    is_hero = False
    
    def __init__(self):
        super().__init__('Hero', 100, 5, 0, 0)

    def critical(self):
        self.power += self.power
    
class Goblin(Character):
    
    is_hero = False
    
    def __init__(self):
        super().__init__('the goblin', 6, 3, 0)

class Zombie(Character):
    
    is_hero = False
    
    def __init__(self):
        super().__init__('the zombie', math.inf, 4, 0 )

class Medic(Character):
    
    is_hero = False
    
    def __init__(self):
        super().__init__('Medic', 30, 5, 4, 4)
        
    def heal(self):
        self.health += 5

class Shadow(Character):
    
    is_hero = False
    
    def __init__(self):
        super().__init__('Shadow', 1, 5, 0, 0)

class Cave_Dweller(Character):

    is_hero = False
    
    def __init__(self):
        super().__init__('the cave dweller', 50, 6, 2, 2)
    
    def berzerk(self):
        self.health += 3
        self.power += 3

class Temple_Gaurd(Character):
    
    is_hero = False
    
    def __init__(self):
        super().__init__('Temple Gaurd', 30, 7, 4)
    
    def heavy(self):
        self.power *= 2
 