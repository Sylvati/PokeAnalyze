# This class is used for running commands.
import subprocess 

# Used for regex
import re

# Used for permutations
from itertools import permutations

# Will store the weight of various happenings.
# For use in the evaluate position
eval_weight = {
    "faint": 1
}

# Input a game log and get an evaluation returned.
def evaluate_position(game_log):
    # This is how we will compare "winning" and "losing"
    # Kinda inspired by chess?
    # p1 is +, p2 is -
    game_evaluation = 0

    # Gets faint lines using regex
    # ^ = start of the line
    # .* = zero or more characters
    # \b = begin word border
    # \b = end word border
    # .* = zero or more characters
    # $ = end of the line
    # Combined effect? Gets the lines where pokemon
    # faint data is contained.
    faints = re.findall(r"^.*\bfaint\b.*$", game_log, re.MULTILINE)
    if len(faints) > 0:
        for faint in faints:
            if "p1" in faint:
                #print(f"[-{eval_weight["faint"]}] Player 1 had a poke faint.")
                game_evaluation -= eval_weight["faint"]
            if "p2" in faint:
                #print(f"[+{eval_weight["faint"]}] Player 2 had a poke faint.")
                game_evaluation += eval_weight["faint"]
    #else:
        #print(f"[0] No players had any pokes faint.")
        

    return game_evaluation

# Team functions

# Give it a path, get a packed team
def load_and_pack_team(path):
    result = subprocess.run(f"node pokemon-showdown-access.js pack-file {path}", capture_output=True)
    return result.stdout.decode().strip()

# Give it a path, get a json team
def load_and_json_team(path):
    result = subprocess.run(f"node pokemon-showdown-access.js get-json-of-file {path}", capture_output=True)
    return result.stdout.decode().strip()

# Give it a path, get a packed team, supports debug
def get_path_load_and_pack_team(path=""):
    if(path == "debug11"):
        path = "example-teams\\WolfeGlick-worlds-2016.txt"
    elif(path == "debug12"):
        path = "example-teams\\JonathanEvans-worlds-2016.txt"
    else:
        path = input("Enter relative path: ")
        path.replace("\n", " ").replace("\\", "\\\\")
        
    return load_and_pack_team(path)

# Format functions

# Gets the format, support for debug
def get_format(format=""):
    if(format == "debug1"):
        format = "gen6vgc2016"
    else:
        format = input("Enter desired format: ")

    return format.replace("\n", " ")

# Simulation functions

def sim(format, name_one, packed_team_one, name_two, packed_team_two, additional_commands=None):
    command = f"node pokemon-showdown-access.js sim {format} {packed_team_one} {packed_team_two} {name_one} {name_two}"
    if additional_commands:
        for additional_command in additional_commands:
            command+= f" {additional_command}"
    result = subprocess.run(command, capture_output=True)
    return result.stdout.decode()

# Wrapper for the sim function so that we can actually use it in a multi-threaded way.
def sim_threading_wrapper(format, name_one, packed_team_one, name_two, packed_team_two, additional_commands=None, result_queue=None):
    result = sim(format, name_one, packed_team_one, name_two, packed_team_two, additional_commands)
    result_queue.put(result)

# Misc. helper functions

# Quick function to resolve a number tuple to a string
def num_tuple_to_string(tuple_to_convert):
    ret_str = ""
    for num in tuple_to_convert:
        ret_str += str(num)
    return ret_str

# Quick function to support debugging when getting the filename
def get_filename(filename=""):
    if(filename == "debug1"):
        filename = "data.json"
    else:
        filename = input("Where should the game tree be stored: ")

    return filename

# Function to generate teampreview permutations
def generate_teampreview_permutations(n, k):
    # Returns every permutatoin of a list from 1 to n
    # when choosing k items.
    # In pokemon words, n will probably ALWAYS be 6
    # and since people will probably use this for VGC Worlds,
    # k will almost definitely be 4.
    # To be honest, wouldn't be a bad idea to use dynamic programming
    # to save the values that are common.
    # This is only ran one time at teampreview though, so I don't know if
    # its really a big deal.
    return list(permutations(list(range(1, n + 1)), k))
