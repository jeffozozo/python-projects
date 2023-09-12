import random
import copy


class Character:
    def __init__(self, name, level, hitdice, damagemin, damagemax):
        self.name = name
        self.level = level
        self.hitpoints = hitdice*level
        self.alive = True
        
        if level > 5:
            damagemax = damagemax + level
        
        self.damagemin = damagemin
        self.damagemax = damagemax
        
    def stats(self,str_class):
        if self.hitpoints <= 0:
            print(self.name + " is dead.")
        else:
            print(self.name + ", level " + str(self.level) +" "+ str_class+ " - Hitpoints " + str(self.hitpoints))

    def attack(self,attack_string,monster):
        damage = random.randrange(self.damagemin,self.damagemax)
        print(self.name + " "+ attack_string + " the " + monster.name + " for "+ str(damage) + " points of damage.")
        monster.take_damage(damage)
    
    def take_damage(self,damage):
        self.hitpoints -= damage
        if self.hitpoints <= 0:
            print(self.name + " has died.")
            self.alive = False
            


class Monster:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.level = 1
        self.hitpoints = self.level*random.randrange(2,6)
        self.damagemin = 1
        self.damagemax = 4
        self.alive = True
        self.hitdice = 1
        self.weapons = []
        
    def attack(self, player):
        damage = random.randrange(self.damagemin,self.damagemax)
        weapon = random.choice(self.weapons)
        print(self.name + " attacks "+ player.name + " with its " + weapon + " for "+ str(damage) + " points of damage.")
        player.take_damage(damage)
        
    def take_damage(self,damage):
        self.hitpoints -= damage
        print(self.name + " has " + str(self.hitpoints))
        if self.hitpoints <= 0:
            print(self.name + " has been killed!")
            self.alive = False
            


class Thief(Character):
    
    def __init__(self, name, level):
        damagemin = 1
        damagemax = 6
        hitdice = 4    
        
        super().__init__(name,level,hitdice,damagemin,damagemax)
        
    def stats(self):
        super().stats("Theif")
       
    def attack(self,monster):
        super().attack("back stabs",monster)
       
        
class Fighter(Character):
    
    def __init__(self,name,level):
        damagemin = 2
        damagemax = 12
        hitdice = 8
        
        super().__init__(name,level,hitdice,damagemin,damagemax)

    def stats(self):
        super().stats("Fighter")
 
    
    def attack(self,monster):
        super().attack("swings a sword at",monster)



class Wizard(Character):
    
    def __init__(self,name,level):
        damagemin = 1
        damagemax = 8
        hitdice = 4
    
        super().__init__(name,level,hitdice,damagemin,damagemax)
        
    def stats(self):
        super().stats("Wizard")
 
        
    def attack(self,monster):
       super().attack("casts a spell at",monster)
       

class Game:
    def __init__(self,difficulty):
        self.current_location = 0
        self.monsters = []
        self.current_monster = None
        self.party = []
        self.difficulty = difficulty

        #locations
        self.locations = ["You are at the mouth of a dark forest. A path leads ahead of you into the forest. The trees are oak, sycamore and fir. The path is rocky and moss covered.",
                      "You're on a rocky path at the mouth of the forrest. The air smells clean and earthy. Light filters through the gaps in the tall trees. Small animals scuttle away at your arrival",
                      "The rocky path leads up a short hill. In the distance you can hear a rushing stream.",
                      "You are at the top of a short hill. The trees are getting thicker, closer together. Light the shade is deep. A small stream is near by.",
                      "The path leads through a small but swift running stream."]
        #monsters
        monster = Monster("Goblin", "You see a slimy, small humanoid with green skin, big ears and sharp teeth.")
        monster.level = 3
        monster.hitdice = 4
        monster.damagemin = 1
        monster.damagemax = 4
        monster.weapons = ["club","rusty knife","flail","bare hands"]
        self.monsters.append(monster)

        monster = Monster("Giant Spider", "In a thick, sticky web, a massive shiny black spider sits making angry clicking sounds.")
        monster.level = 2
        monster.hitdice = 6
        monster.damagemin = 2
        monster.damagemax = 8
        monster.weapons = ["fangs","poison spit","front legs","spinnerettes"]
        self.monsters.append(monster)
        
        monster = Monster("Dire Wolf","There is a giant dark grey wolf with red eyes here.")
        monster.level = 4
        monster.hitdice = 4
        monster.damagemin = 4
        monster.damagemax = 12
        monster.weapons = ["fangs","claws"]
        self.monsters.append(monster)

    def help(self):
        print("look - tells you about the location you are at or the puzzle you're in.")
        print("forward - takes you to the next location. You won't be able to do this if you are in a fight.")
        print("attack - engages a monster or enemy")
        print("sneak - attempts to sneak by a monster or enemy.")
        print("help - lists the options.")
        print("hint - gives you a hint for how to solve a puzzle.")
     
    def print_location(self):
        print()
        print(self.locations[self.current_location])
        if self.current_monster is not None:
            if self.current_monster.alive:
                print(self.current_monster.description)
            else:
                print("There is a dead "+self.current_monster.name+" here.")
            
        
    def test_for_monster(self):      
        if self.current_monster is None and random.randrange(0,10) < self.difficulty:
            monster = random.choice(self.monsters)
            self.current_monster = copy.deepcopy(monster)
            
        
    def prompt(self):
        return input("What would you like to do? :")
    
    def handle_attack(self):
        if self.current_monster is None:
            print("there is nothing to attack.")
            return
        
        if not self.current_monster.alive:
            print("You already killed the "+self.current_monster.name+".")
            return

        print()
        print("You attack the " + self.current_monster.name +"!")
        number_in_party = len(self.party)
        party_ok = True
        while(self.current_monster.alive):
            if not party_ok:
                print("All of the party members are dead.")
                break
            # loop through each person in the party, but check to see if the monster gets an attack in between
            for count in range(number_in_party):
                #if the toss is high, the monster attacks
                if random.randrange(0,10) < self.difficulty: 
                    player = random.choice(self.party)
                    self.current_monster.attack(player)
                else:
                    self.party[count].attack(self.current_monster)
                    #if monster is dead, break out of the loop
                    if self.current_monster.hitpoints <= 0:
                        break
                    
            #as long as one party member is still alive, keep going
                party_ok = False
                for player in party:
                    if player.alive:
                        party_ok = True
                        
    def handle_sneak(self):
        if self.current_monster is None:
            print("There's no monster about. Don't you feel a little silly sneaking.")
            self.current_location += 1
            return
        
        if self.current_monster.alive:
            if random.randrange(0,10) < self.difficulty:
                player = random.choice(self.party)
                print(player.name + " made some noise. The "+ self.current_monster.name + " looks right at you and attacks!")
                self.handle_attack()
            else:
                print("You sneak quietly by the "+self.current_monster.name)
                self.current_location += 1
                self.current_monster = None
                
    def party_stats(self):
        print()
        print("There are " + str(len(self.party))+" people in your party with the following stats")
        for p in self.party:
            p.stats()
    
    
    def do(self,command):
    
        match command:
            case "help" | "h" :
                self.help()
            
            case "attack" | "a" :
                self.handle_attack()
        
            case "look"|"l" :
                # you're going to see again anyway - this is essentially a no-op
                print()
                
            case "sneak" | "s":
                self.handle_sneak()
                
            case "stats" | "st":
                self.party_stats()
                
            case "exit" | "quit" | "q" | "e":
                if input("Are you sure you'd like to quit? (y/n)") == "y":
                    return "exit"
                
            case "forward" | "f":
                if self.current_monster is not None and self.current_monster.alive:
                    print("You can't go anywhere with that monster staring at you.")
                else:
                    self.current_location += 1
                    self.current_monster = None
                
        return "keep playing"
                 
        
        

# Start Game

the_game = Game(7)

#set up players
party = []

player = Thief("Theodore",3)
party.append(player)

player = Fighter("Gug",3)
party.append(player)

player = Wizard("Zippo",4)
party.append(player)

the_game.party = party

print("Welcome to the Adventure Game!")
print("In this simple game, you'll need to use your imagination. You are traveling along a road through a forest on the way to a castle.")
print("You will encounter monsters and tricky situations. You'll need your wits to survive.")
print("Press Enter to begin. (you can type 'help' at any time for a list of things you can do)")
input()

print()
print()

the_game.party_stats()

print()





#game loop

answer = " "

while(answer != "exit"):


    the_game.test_for_monster()
    the_game.print_location()
    answer = the_game.prompt()
    answer = the_game.do(answer)
    
    















