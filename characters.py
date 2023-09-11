import random

class Thief:
    
    def __init__(self, name, level):
        self.name = name
        self.level = level;
        self.hitpoints = random.randrange(4,4*level)
        
    def stats(self):
        print(self.name + ", level " + str(self.level) + " Thief - Hitpoints " + str(self.hitpoints))
       
    def attack(self):
        damage = random.randrange(1,8)
        print(self.name + " back stabs for " + str(damage) + " points of damage.")
        return damage
        
        
class Fighter:
    
    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.hitpoints = random.randrange(8,8*level)
        
    def attack(self):
        damage = random.randrange(2,12)
        print(self.name + " swings a sword for " + str(damage) + " points of damage.")
        return damage

    def stats(self):
        print(self.name + ", level " + str(self.level) + " Fighter - Hitpoints " + str(self.hitpoints))


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

    
    

a_goblin = Goblin(3)
a_thief = Thief("Timmy",3)
a_fighter = Fighter("Thump",2)

a_thief.stats()
a_fighter.stats()

print("A goblin is attacking you!")

a_goblin.attack()

print("Your turn.")

a_thief.attack()
a_fighter.attack()





