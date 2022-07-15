

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
            if i == 'Armor':
                pc.armor_rating += 2
                pc.item_list.remove('Armor')
                break

    def Evade (self, pc):
        for i in pc.item_list:
            if i == 'Evade':
                pc.evade += 2
                pc.item_list.remove('Evade')
                break
            
    def Root (self, pc):
        for i in pc.item_list:
            if i == 'Root of the Mutant Tree':
                pc.power += 2
                pc.item_list.remove('Root of the Mutant Tree')
                break
            
    def Remove_Root(self, pc):
        pc.power -= 2

                
            
        
    



        