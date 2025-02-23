# This class is used for running commands.
import subprocess 

import re

def evaluate_position(game_log):
    # Will store the weight of various happenings.
    eval_weight = {
        "faint": 1
    }

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
                print(f"[-{eval_weight["faint"]}] Player 1 had a poke faint.")
                game_evaluation -= eval_weight["faint"]
            if "p2" in faint:
                print(f"[+{eval_weight["faint"]}] Player 2 had a poke faint.")
                game_evaluation += eval_weight["faint"]
    else:
        print(f"[0] No players had any pokes faint.")

    return game_evaluation