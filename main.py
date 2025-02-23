# ================================
#       SECTION: Imports
# ================================

# Putting completed functions in here
import pokemon_showdown_cli_helper as pcli

# We need this to check if file exists before
# doing all the work to calculate 
from os import path

# We need this for multithreading
import threading

# We need this to collect our results from multi threading
import queue

# For saving and loading
import json
from poke_tree import PokeNodeEncoder
from poke_tree import PokeNodeDecoder

# Way to store the game states
from poke_tree import PokeNode
root = PokeNode("root")
# =====================================
#           Design Outline
# =====================================

debug = True

# ================================
#       SECTION: Team Loading
# ================================

# Load team 1
team_one_packed_team = pcli.get_path_load_and_pack_team("debug11")

# Load team 2
team_two_packed_team = pcli.get_path_load_and_pack_team("debug12")

# ================================
#       SECTION: Rules
# ================================

# Get format from user
format = pcli.get_format("debug1")

# ================================
#       SECTION: Lead Generation and Execution
# ================================

# This is slightly different from other move phases
# Because of some formats having team preview
# (most, if not all VGC formats)
# And those formats having pokemon choice
# We need to generate all possible leads and back choices
# In reality this means generating 
# all the possible combinations of 123456
# order matters, no repetition
# permutations maybe?? I think

# Get the filename to store the data in
filename = pcli.get_filename("debug1")

# Create the root node
root = PokeNode(pcli.sim(format, "Player 1", team_one_packed_team, "Player 2", team_two_packed_team))

# Check if the file already exists
already_exists = path.isfile(filename)

# If it does, load it
if(already_exists):
    # Opens the file and loads the root node
    # (Which will inherently load the children nodes)
    with open(filename, 'r') as file:
        root = json.load(file, cls=PokeNodeDecoder)

# If it doesn't we need to run the permutations of teampreview
else:
    # Check if we are currently in the teampreview phase
    if(root.get_phase() == "teampreview"):
        num_pokemon_to_choose = root.get_number_of_pokemon_to_teampreview()

        full_party = 6 # We make a variable for this solely to avoid the issue of "where did this # come from??"
        possible_choices = pcli.generate_teampreview_permutations(full_party, num_pokemon_to_choose)
        
        # So, how do we now continue the simulation?
        # We need to write
        # >p1 team 1234(permutation)
        # then 
        # >p2 team 1234(permutation)
        # we can't have spaces.. so. why not use a filler character?

        # Test every permutation
        successes = 0
        result_queue = queue.Queue()

        successes = 0
        threads = []
        result_queue = queue.Queue()
        for possible_choice in possible_choices:
            # Create the lead choice
            command_to_add = ">p1 team " + pcli.num_tuple_to_string(possible_choice)

            # Create the thread that runs the simulation we want it to run.
            new_thread = threading.Thread(target=pcli.sim_threading_wrapper, args=("gen6vgc2016", "Wolfe_Glick", team_one_packed_team, "Jonathan_Evans", team_two_packed_team, [command_to_add.replace(" ", "|"),">p2 team 1234".replace(" ", "|")], result_queue))
            
            # Add that thread to the list of threads we must run
            threads.append(new_thread)

        # Begin every thread simultaneously
        for thread in threads:
            thread.start()

        # Block until all threads are complete
        for thread in threads:
            thread.join()

        # Go through the queue that holds our results and append them as new "gamestates" to the root node
        while not result_queue.empty():
            root.child.append(PokeNode(result_queue.get()))

        # Check to make sure everything worked
        for node in root.child:
            if("|turn|1" in node.pokemon_showdown_log):
                successes += 1

        # Should print 360
        print(successes)
        
        # Save result
        with open(filename, 'w') as file:
            json.dump(root, file, indent=4, cls=PokeNodeEncoder)

# ================================
#       SECTION: Tree culling
# ================================

# These operations are gonna get expensive fast, so what we need to do
# is quickly cull nodes where the positive evaluation decreases.
# Therefore, we need to search through every possibility and only continue down the paths that have the highest evaluation
# Unfortunately for team leads, this is extremely unlikely to change and most leads are probably going to be the same (?)
# Unless I find some way of evaluating that.
# Therefore, I'm probably gonna have to evaluate all like, 4096 possibilites on all 360 leads, which is like
# 1,474,560 possibilities, which is going to take FOREVER.

# https://github.com/smogon/damage-calc
# This may be an interesting website to change evaluation.
# Perhaps evaluate who has more 1 OHKO, 2 OHKO, or 3 OHKOs?

# ================================
#       SECTION: Move Generation
# ================================

# Generate all possible moves and swaps
# Includes mega/non-mega
# do this in python

# ================================
#       SECTION: Move execution
# ================================

# Run the moves in the NodeJS

# ================================
#       SECTION: Eval
# ================================

# Evaluate all the possible moves in python
# Once again, store them

# ================================
#       SECTION: Repeat 
#       last 3 steps until
#       game is over
# ================================

# ================================
#       SECTION: Win/Loss
#       Culling
# ================================

# Do not need to continue the process when a game is
# won or lost, so just cull.