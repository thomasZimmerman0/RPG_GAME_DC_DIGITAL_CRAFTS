

class Items:

    def __init__(self, name):
        self.name = name
        
    def SuperTonic(self, pc):
        for i in pc.item_list:
            if i == 'SuperTonic':
                pc.health += 10
                pc.item_list.remove('SuperTonic')
                break
                
    def Armor(self, pc):
        for i in pc.item_list:
            if i == 'Old Leather Pads':
                pc.armor_rating += 2
                pc.item_list.remove('Old Leather Pads')
                break

    def Evade (self, pc):
        for i in pc.item_list:
            if i == 'Rune of Evasion':
                pc.evade += 2
                pc.item_list.remove('Rune of Evasion')
                break
            
    def Root (self, pc):
        for i in pc.item_list:
            if i == 'Root of the Mutant Tree':
                pc.power += 2
                pc.item_list.remove('Root of the Mutant Tree')
                break
            
    def Remove_Root(self, pc):
        pc.power -= 2
    
    def Swap(self, pc, npc):
        hold = pc.power
        for i in pc.item_list:
            if i == 'Scroll of Reversal':
                pc.power = npc.power
                npc.power = hold
                pc.item_list.remove('Scroll of Reversal')
                break
    
    def Dull_Sabre(self, pc):
        for i in pc.item_list:
            if i == 'Dull Sabre':
                pc.power += 3
                pc.item_list.remove('Dull Sabre')
                break
            
    def Remove_Dull_Sabre(self, pc):
        pc.power -= 3

                
            
        
    



        