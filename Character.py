class Character:
    
    
    chance_success = False
    
    
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    
    #! Checks to see if the character is still alive
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
        
    #! Prints health and power of the character
    def print_status(self):
        if self.is_hero == True:
            print(f"You have {self.health} health and {self.power} power.")
        elif self.is_hero == False:
            print(f"{self.name} has {self.health} health and {self.power} power.")
    
    
    #! Takes in 2 characters and performs multiple calculations and prints accordingly 
    #? Character based calculations are performed and checked within this method
    def attack(self, character):
        
        self.rng20() #calls for a 20% chance of success for hero's (the player's) critical hit
        orig_power = self.power #holds original value for power
        
        if self.chance_success == True and isinstance(self, Hero): #Will currently only work on Hero character
            self.critical() #Temporarily double's hero's damage if successful
        
        if isinstance(character, Shadow): 
            character.rng10()
            if character.chance_success == False:
                self.power = 0
            
            
            
        character.health -= self.power #! Health diminishment calculation! All damage mutlipliers should be done before this line!
        
        
        
        if self.is_hero == True: #Runs if it is the player character attacking
            print(f"You do {self.power} damage to {character.name}.")
            self.power = orig_power #Resets multiplier if it was successful
            
            
            if isinstance(character, Medic):                #Performs Medics special ability 
                character.rng20()                           #for a chance to heal after being 
                if character.chance_success == True:        #attacked by the player
                    character.health += 2
                    print(f"{character.name} healed!")
                    
                    
            if character.alive() == False:
                print(f"{character.name} is dead.")
                
        elif self.is_hero == False: #Runs if it is an npc attacking, 
            print(f"{self.name} does {self.power} damage to {character.name}.")
            if character.alive() == False:
                print("You are dead.")
                
                
    
    #! Random number generator used to determine if a probability based attack / defense will succeed
    def rng20(self):
        number = random.randrange(1, 100)
        if number <= 20:
            self.chance_success = True
        else: 
            self.chance_success = False
    
    
    #! Same as rng20 but is only returns true 10% of the time
    def rng10(self):
        number = random.randrange(1, 100)
        if number <= 10:
            self.chance_success = True
        else: 
            self.chance_success = False