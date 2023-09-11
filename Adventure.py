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


class Monster:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.level = 1
        self.hitpoints = self.level*random.randrange(1,2)
        self.damagemin = 1
        self.damagemax = 4
        
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
       



class Game:
    def __init__(self):
        self.current = 0
        self.monsters = []
        self.current_monster = None
        
        #locations
        self.locations = ["You are at the mouth of a dark forest. A path leads ahead of you into the forest. The trees are oak, sycamore and fir. The path is rocky and moss covered.",
                      "You're on a rocky path at the mouth of the forrest. The air smells clean and earthy. Light filters through the gaps in the tall trees. Small animals scuttle away at your arrival",
                      "The rocky path leads up a short hill. In the distance you can hear a rushing stream.",
                      "You are at the top of a short hill. The trees are getting thicker, closer together. Light the shade is deep. A small stream is near by.",
                      "The path leads through a small but swift running stream."]
        #monsters
        monster = Monster("Goblin", "a slimy, small humanoid with green skin, big ears and sharp teeth.")
        monster.level = 3
        monster.hitdice = 4
        monster.damagemin = 1
        monster.damagemax = 4
        monster.weapons = ["club","rusty knife","flail","bare hands"]
        self.monsters.append(monster)

        monster = Monster("Giant Spider", "a massive shiny black spider.")
        monster.level = 2
        monster.hitdice = 6
        monster.damagemin = 2
        monster.damagemax = 8
        monster.weapons = ["fangs","poison spit","front legs","spinnerettes"]
        self.monsters.append(monster)
        
        monster = Monster("Dire Wolf","giant dark grey wolf with red eyes.")
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
        print(self.locations[self.current])
        if self.current_monster is not None:
            print(self.current_monster.description)
            
        
    def monster_appears(self):
        self.current_monster = random.choice(self.monsters)
        return self.current_monster.description
    
    def do(self,command):
    
        match command:
            case "help" | "h" :
                self.help()
            
            case "attack" | "a" :
                print("you attack")
        
            case "look"|"l" :
                self.print_location()
        
        

# Start Game

the_game = Game()

#set up players
players = []

player = Thief("Timmy",3)
players.append(player)

player = Fighter("Gug",3)
players.append(player)

player = Wizard("Zippo",4)
players.append(player)


print("Welcome to the Adventure Game!")
print("In this simple game, you'll need to use your imagination. You are traveling along a road through a forest on the way to a castle.")
print("You will encounter monsters and tricky situations. You'll need your wits to survive.")
print("Press Enter to begin. (you can type 'help' at any time for a list of things you can do)")
input()



print("There are three people in your party with the following stats")
for p in players:
    p.stats()

print()

#game loop

while(True):

    if random.randrange(0,10) > 1:
        monster = the_game.monster_appears()


#command loop
    while(True):
        the_game.print_location()

        #prompt
        print("What would you like to do?")
        print(":")
        answer = input()
        if answer == "exit":
            break
        
        the_game.do(answer)
    


#actions: look, attack, sneak, quit,












