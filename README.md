# PokeAnalyze (Name Subject to Change)

PokeAnalyze uses Pokémon Showdown’s local Node.js implementation to analyze battle states using a tree-based approach. By evaluating stored states, the tool aims to determine the best move based on the highest-rated game scenarios. 

This project is in its early stages, and contributions are welcome! If you’re passionate about competitive Pokémon battling, AI-driven decision-making, or optimization, your help would be greatly appreciated.

## Features & Goals

- **Battle State Analysis**: Stores and evaluates Pokémon battle states in a tree where each battle state is analyzed.
- **Win Percentage Estimation**: Uses combinatorics to approximate win rates between teams without running every possible simulations, since Pokémon has nearly infinite simulation possibilities.
- **Competitive Team Comparison**: Helps make team analysis easier by getting win percentages that can be compared to find what teams work better against other teams.
- **Potential Future Applications**: If developed further, this tool could be used to create advanced AI opponents for Pokémon ROM hacks or simulations.

## Installation

### Prerequisites 
- Python 3.x
- Node.js

### Setup
1. Clone the repository:
```sh
git clone https://github.com/Sylvati/PokeAnalyze
cd PokeAnalyze
```
2. Install dependencies
```sh
pip install -r requirements.txt
```

## Usage
Currently, it doesn't make much sense to actually use the tool as it is not developed enough to be useful. However, the main access point will be:
```sh
python main.py
```

## Development Roadmap

- **Improving the Evaluation Function:** Currently the model only gives points based on faints, which really sucks. This is where I need the most help as I am a novice competitive Pokemon battler, so I don't really know what is best.
	- **File:** `pokemon-showdown-cli-helper.py`
	- **Function:** `evaluate_position(game_log):`
	- **Evaluation Dictionary:** `eval_weight`
- **Optimize Simulation Performance:** Battles currently take ~2-3 seconds each. Basic multithreading reduces 360 simulations to ~40-60 seconds, but further optimization is needed.
	- **File:** `main.py`
	- **Relevant Code:** Lines 100-122
	- **Issues:** Blue screened my pc once. 
- **Enhance Stability of Multi-threading:** Threads are improperly managed currently, I think. Which leads to crashes. Need to explore ThreadPools or other multi-processing options.
- **GUI Development (Future Plan):** Eventually, a user-friendly interface needs to be added because only computer science people like CLI programs.

## File Overview
- `test.ipynb` - this is usually where I write all the code to test it, but I'm moving away from that because I have learned that Jupyter notebooks are not great at testing multi-threading, and mostly everything is probably gonna need to be multi-threaded.
- `unit_testing.py` - Placeholder for unit tests (no code there yet 🙃)
- `pokemon-showdown-access.js` - Interfaces Python scripts with Pokémon Showdown via `os.subprocess()`

## Goals
To basically be StockFish for pokemon. Much harder than it sounds since Pokemon has infinitely many positions while chess has a countable number of positions. (I think)

## Contributing

This is my first open-source project, so I’m learning best practices along the way. If you’d like to contribute:

1.  Fork the repository.
2.  Create a new branch (`feature-branch`).
3.  Submit a Pull Request (PR) with a detailed explanation of your changes.

Need help? Open an issue or suggest improvements in the discussions!

Also, feel free to suggest how to properly credit contributors. It is important that everyone is credited.

## License
I want to support FOSS (Free and Open Source Software) so the license I have chosen is the GNU GPLv3 license.


== We're Using GitHub Under Protest ==

This project is currently hosted on GitHub.  This is not ideal; GitHub is a
proprietary, trade-secret system that is not Free and Open Souce Software
(FOSS).  We are deeply concerned about using a proprietary system like GitHub
to develop our FOSS project.  

We urge you to read about the
[Give up GitHub](https://GiveUpGitHub.org) campaign from
[the Software Freedom Conservancy](https://sfconservancy.org) to understand
some of the reasons why GitHub is not a good place to host FOSS projects.

Any use of this project's code by GitHub Copilot, past or present, is done
without our permission.  We do not consent to GitHub's use of this project's
code in Copilot.

![Logo of the GiveUpGitHub campaign](https://sfconservancy.org/static/img/GiveUpGitHub.png)