
# For this assignment, load in your sys.argv like so:
# duck_goose = sys.argv[1:]
# The above duck_goose a list-type variable which contains lower-cased
# words, either 'duck' or 'goose' (ex. [ 'duck', 'duck', 'goose']).

# ● Create a program, duckgoose.py which removes all the ‘goose’ within the list
# then print the remaining list.

import sys

# Load variable from command-line argument
duck_goose = sys.argv[1:]

# Remove all occurrences of 'goose' from the list
remaining_list = [word for word in duck_goose if word.lower() != 'goose']

# Print the remaining list
print(remaining_list)

#RUN THESE PLEASE
#python duckgoose.py goose duck duck goose goose
#python duckgoose.py goose goose goose goose
#python duckgoose.py duck duck duck duck