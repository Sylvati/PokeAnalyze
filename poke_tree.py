# For using custom functions like evaluation
import pokemon_showdown_cli_helper as poke_cli

# For saving and loading
from json import JSONEncoder
from json import JSONDecoder

# For doing regex
import re

# Credit where credit is due
# I stole most of this code from
# https://www.geeksforgeeks.org/generic-tree-level-order-traversal/

# Encoder so we can use JSON to save
# We use this with this command:
#json.dumps(root, indent=4, cls=PokeNodeEncoder)
class PokeNodeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
    
# Decoder so that we can use JSON to load
class PokeNodeDecoder(JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.object_hook)

    def object_hook(self, d):
        # Ensure the dictionary contains the necessary keys before converting
        if "key" in d and "child" in d and "pokemon_showdown_log" in d and "last_line" in d and "phase" in d:
            return PokeNode(d)
        return d  # Return the dictionary as is if it doesn’t match


class PokeNode:
    def __init__(self, *args):
        if(isinstance(args[0], str)):
            pokemon_showdown_log = args[0]
            self.key = poke_cli.evaluate_position(pokemon_showdown_log)
            self.child = []
            self.pokemon_showdown_log = pokemon_showdown_log
            self.last_line = None
            self.phase = None
        elif(isinstance(args[0], dict)):
            self.key = args[0].get("key")
            self.child = args[0].get("child")
            self.pokemon_showdown_log = args[0].get("pokemon_showdown_log")
            self.last_line = args[0].get("last_line")
            self.phase = args[0].get("phase")

    # Function to get the phase cus we need to make sure its checked first
    def get_phase(self):
        if(self.phase != None):
            return self.phase
        
        self.check_phase()
        return self.phase

    # Function that checks if we are in teampreview phase
    def check_phase(self):
        last_line = self.get_last_line()

        if("teampreview" in last_line):
            self.phase = "teampreview"
    
    # Function to save calls to get the last line. I'm assuming its an expensive call.
    def get_last_line(self):
        if(self.last_line != None ):
            return self.last_line
        
        self.last_line = self.pokemon_showdown_log.splitlines()[-1]
        return self.last_line
    
    # Gets the amount of pokemon to select from the teampreview line.
    # Makes sure that we are in the teampreview phase
    def get_number_of_pokemon_to_teampreview(self):
        if("teampreview" not in self.get_last_line()):
            print("Error, can't get the amount of teampreview pokemon from a node not in teampreview phase.")
            return
        
        return int(re.findall(r"[0-9]", self.get_last_line())[0])

# Prints the n-ary tree level wise
def LevelOrderTraversal(root):
 
    if (root == None):
        return
   
    # Standard level order traversal code
    # using queue
    q = []  # Create a queue
    q.append(root); # Enqueue root 
    while (len(q) != 0):
     
        n = len(q)
  
        # If this node has children
        while (n > 0):
         
            # Dequeue an item from queue and print it
            p = q[0]
            q.pop(0)
            print(p.key, end=' ')
   
            # Enqueue all children of the dequeued item
            for i in range(len(p.child)):
             
                q.append(p.child[i])
            n -= 1
   
        print() # Print new line between two levels
