import chara

class Items:

    def __init__(self, name):
        self.name = name
    
    def use_item(self, pc, npc):
        for i in pc.item_list:
            if isinstance(self, Swap):
                self.bonus(pc, npc)
                pc.item_list.remove(self.name)
            else:
                self.bonus(pc)
                pc.item_list.remove(self.name)
            break
            

class SuperTonic(Items):
    def __init__(self):
        super().__init__('SuperTonic')
    
    def bonus(self, pc):
        if pc.health < 45 and isinstance(pc, chara.Hero):
            if pc.health > 35:
                pc.health = 45
            else:
                pc.health += 10
                
        if pc.health < 55 and isinstance(pc, chara.Medic):
            if pc.health > 45:
                pc.health = 55
            else:
                pc.health += 10
                
        if pc.health <= 35 and isinstance(pc, chara.Assassian):
            if pc.health > 25:
                pc.health = 35
            else:
                pc.health += 10
            
        
        
class Armorlv1(Items):
    
    
    
    def __init__(self):
        super().__init__('Old Leather Pads')
        
        
    def bonus(self, pc):
        pc.armor_rating += 2
        
    def remove(self, pc):
        pc.armor_rating -= 2
        
        
class Armorlv2(Items):
    
    
    
    def __init__(self):
        super().__init__('Used Chainmail Garb')
        
        
    def bonus(self, pc):
        pc.armor_rating += 5
        
    def remove(self, pc):
        pc.armor_rating -= 5
        
        
class Armorlv3(Items):
    
    
    
    def __init__(self):
        super().__init__('New Mastercrafted Knights Suit of Armor')
        
        
    def bonus(self, pc):
        pc.armor_rating += 10
        
    def remove(self, pc):
        pc.armor_rating -= 10
        
        
class Evade(Items):
    def __init__(self):
        super().__init__('Rune of Evasion')
        
    def bonus(self, pc):
        pc.evade += 1
        
class Root(Items):
    def __init__(self):
        super().__init__('Root of the Mutant Tree')
        
    def bonus(self, pc):
        pc.power += 2
    
    def remove_root(self, pc):
        pc.power -= 2
        
class Swap(Items):
    def __init__(self):
        super().__init__('Scroll of Reversal')
        
    def bonus(self, pc, npc):
        hold = pc.power
        pc.power = npc.power
        npc.power = hold
        
class Swordlv1(Items):
    
    
    
    def __init__(self):
        super().__init__('Dull Sabre')
        
        
    def bonus(self, pc):
        pc.power += 3
    
    def remove(self, pc):
        pc.power -= 3
        
        
class Swordlv2(Items):
    
    
    
    def __init__(self):
        super().__init__('Knight\'s Longsword')
        
        
    def bonus(self, pc):
        pc.power += 5
    
    def remove(self, pc):
        pc.power -= 5
        
        
class Swordlv3(Items):
    
    
    
    def __init__(self):
        super().__init__('Arch Bishop Igor\'s Legnedary Diamond Encrusted Two-handed Great Sword')
        
        
    def bonus(self, pc):
        pc.power += 8
    
    def remove(self, pc):
        pc.power -= 8
        
        
class Volatile_Powder(Items):
    def __init__(self, used):
        super().__init__('Volatile Powder')
        self.used = used
    
    def bonus(self, pc):
        self.used = True
        
                
            
        
    



        