# This class is used for running commands.
import subprocess 

# Used for regex
import re

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

def load_and_pack_team(path):
    result = subprocess.run(f"node pokemon-showdown-access.js pack-file {path}", capture_output=True)
    return result.stdout.decode().strip()

def get_path_load_and_pack_team(path=""):
    if(path == "debug11"):
        path = "example-teams\\WolfeGlick-worlds-2016.txt"
    elif(path == "debug12"):
        path = "example-teams\\JonathanEvans-worlds-2016.txt"
    else:
        path = input("Enter relative path: ")
        path.replace("\n", " ").replace("\\", "\\\\")
        
    return load_and_pack_team(path)

def get_format(format=""):
    if(format == "debug1"):
        format = "gen6vgc2016"
    else:
        format = input("Enter desired format: ")

    return format.replace("\n", " ")