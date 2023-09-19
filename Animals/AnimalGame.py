

class Node:
    
    def __init__(self,val):
        self.yes = None
        self.no = None
        self.val = val
        self.leaf = True
               


def traverse_write(current_node,file):
    
    #visit the current node - pre-order traverse        
    if current_node is None:
        file.write("none,")
        return
    
    file.write(current_node.val+",")

    #visit the yes child
    traverse_write(current_node.yes, file)
    
    #visit the no child
    traverse_write(current_node.no, file)
        

def _traverse_read(current_node,data):
    
    item = data.pop(0)
    if item == "none":
        return
    
    current_node.val = item
    
    #visit the yes child
    current_node.yes = Node("placeholder")
    _traverse_read(current_node.yes,data)
    if current_node.yes.val == "placeholder":
        current_node.yes = None

    #visit the no child
    current_node.no = Node("placeholder")
    _traverse_read(current_node.no,data)
    if current_node.no.val == "placeholder":
        current_node.no = None

    if current_node.no is None and current_node.yes is None:
        current_node.leaf = True
    else:
        current_node.leaf = False


def traverse_read(current_node,file):
    
    data_file = file.read()
    data_list = data_file.split(",")
    _traverse_read(current_node,data_list)
    


#algorithm
# Ask the current question - distinguishing whether the question is a leaf node (has no children) or not. If it is a leaf node, that means that
# we're at an animal, and whether the human answers yes or no to the question, the computer will need to add a new node.
# To add a new node, the computer asks for a new question that will become the 'val' at the current node. Then, depending on how
# the person should answer the question to distinguish between the new animal and the current one, the current animal is assigned
# to either the yes or no node child of the current node, and the new animal is assigned to the other.  
# because the current node now has children, it is no longer a leaf, and it will be set to false so the regular question can be asked.
#
# If were NOT at a leaf node, ask the question and set the current to the yes or no node according to the answer.



print("Hi!  This is a game where YOU think of an animal and I'll try to guess it. If I get it wrong, you can teach me about new animals that I don't know.")
print("I may ask you to write a question - please only use a yes or no question, and try to make it very simple. I'll remember the animals you teach me,")
print("and eventually I'll know a lot. If you want to erase my memory and start over, delete the file called 'animals.dat' in the directory where this program is running.")


# read the data from the file if it is available

try:
    root = Node("temp")
    f = open("animals.dat")
    traverse_read(root,f)
    f.close()
    print()
    print("I loaded a bunch of animals so, I'm pretty smart. See if you can trick me.")

except:
    root = Node("Is it a mammal")
    root.yes = Node("Moose")
    root.no = Node("Frog")
    root.leaf = False
    print("I don't know very many animals, so you'll need to teach me, ok?")
    
print()
print("Think of an animal.")

#set up
current = root
quit = False

#game loop
while(not quit):
    print()
    if current.leaf == True:
        question = "Is it a " + current.val
    else:
        question = current.val

    answer = input(question + "? ")

    if answer == 'y' or answer == 'yes':
        if current.yes is not None:
            current = current.yes
        else:
            print("I guessed it! It was a " + current.val)
            again = input("Play again? (y/n) ")
            if again == 'n': quit = True
            else: current = root
            

    if answer == 'n' or answer == 'no':
        if current.no is not None:
            current = current.no
        else:
            print("Ok, I give up.")
            new_animal = input("What is it? ")
            new_question = input("What is a yes/no question that would distinguish a " + current.val+ " from a " + new_animal + "? ")
            right_answer = input("Ok, now what is the right answer for a " + new_animal + " (y or n)? ")

            if right_answer == 'y':
                current.yes = Node(new_animal)
                current.no = Node(current.val)
            else:
                current.no = Node(new_animal)
                current.yes = Node(current.val)

            current.val = new_question
            current.leaf = False
            
            again = input("Play again? (y/n) ")
            if again == 'n': quit = True
            else: current = root
        
            


# write out the new tree to the file
f = open("animals.dat","w")
traverse_write(root,f)
f.write("end.")
f.close()






    
    





        
        
        
        
        
  
                

    