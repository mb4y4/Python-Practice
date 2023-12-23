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