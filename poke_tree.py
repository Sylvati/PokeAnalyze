import pokemon_showdown_cli_helper as poke_cli

# Credit where credit is due
# I stole most of this code from
# https://www.geeksforgeeks.org/generic-tree-level-order-traversal/

class PokeNode:
    def __init__(self, pokemon_showdown_log):
        self.key = poke_cli.evaluate_position(pokemon_showdown_log)
        self.child = []
        self.pokemon_showdown_log = pokemon_showdown_log
     
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
