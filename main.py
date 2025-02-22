# =====================================
#           Design Outline
# =====================================

# ================================
#       SECTION: Team Loading
# ================================

# Load team 1
# Get filename or path from user
# This should read the text file using python,
# then it should pack the team using the NodeJS

# Load team 2
# Get filename or path from user
# This should read the text file using python,
# then it should pack the team using the NodeJS
# This should probably use a function so I don't
# have to type a bunch of code twice.

# ================================
#       SECTION: Rules
# ================================

# Get format from user
# Find out if its singles, doubles, triples, etc
# The program is gonna be optimized for doubles first
# Because VGC rules are doubles.

# ================================
#       SECTION: Initial Lead Generation
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

# ================================
#       SECTION: Lead execution
# ================================

# Run the leads in the NodeJS

# ================================
#       SECTION: Eval 
# ================================

# Evaluate all the possible leads in python, store
# them in some sort of tree
# make sure this tree is saveable, this gna take lots
# of computing power

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