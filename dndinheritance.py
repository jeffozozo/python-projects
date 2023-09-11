import random


class Character:
    def __init__(self, name, level, hitdice, damagemin, damagemax):
        self.name = name
        self.level = level
        self.hitpoints = hitdice*level
        
        if level > 5:
            damagemax = damagemax + level
        
        self.damagemin = damagemin
        self.damagemax = damagemax
        
    def stats(self,str_class):
        print(self.name + ", level " + str(self.level) +" "+ str_class+ " - Hitpoints " + str(self.hitpoints))

    def attack(self,attack_string):
        damage = random.randrange(self.damagemin,self.damagemax)
        print(self.name + " "+ attack_string + " for "+ str(damage) + " points of damage.")
        return damage


class Thief(Character):
    
    def __init__(self, name, level):
        damagemin = 1
        damagemax = 6
        hitdice = 4
        
        super().__init__(name,level,hitdice,damagemin,damagemax)
        
    def stats(self):
        super().stats("Theif")
       
    def attack(self):
        super().attack("back stabs")
       
        
class Fighter(Character):
    
    def __init__(self,name,level):
        damagemin = 2
        damagemax = 12
        hitdice = 8
        
        super().__init__(name,level,hitdice,damagemin,damagemax)

    def stats(self):
        super().stats("Fighter")
 
    
    def attack(self):
        super().attack("swings a sword")



class Wizard(Character):
    
    def __init__(self,name,level):
        damagemin = 1
        damagemax = 8
        hitdice = 4
    
        super().__init__(name,level,hitdice,damagemin,damagemax)
        
    def stats(self):
        super().stats("Wizard")
 
        
    def attack(self):
       super().attack("casts a spell")
       

class Goblin:
    
    def __init__(self,level):
        self.weapons = ["club","rusty knife","flail","bare hands"]
        self.my_weapon = random.choice(self.weapons)
        self.level = level
        self.hitpoints = random.randrange(3,3*level)
        
    def attack(self):
        damage = random.randrange(2,12)
        print("Goblin attacks with their "+ self.my_weapon + " doing " + str(damage) + " points of damage.")
        return damage


players = []

player = Thief("Timmy",3)
players.append(player)

player = Fighter("Gug",7)
players.append(player)

player = Wizard("Zippo",4)
players.append(player)

print("Character Stats:")
for p in players:
    p.stats()

print()

for p in players:
    p.attack()





