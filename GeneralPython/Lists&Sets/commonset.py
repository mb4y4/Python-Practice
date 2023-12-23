import sys

# Load variables from command-line arguments
set_a = set(sys.argv[1:])
set_b = {'apple', 'banana', 'mango', 'orange'}  # Using a set for set_b

# Find common words between set_a and set_b
common_words = set_a.intersection(set_b)

# Print the output in a set format
print(common_words)

#RUN THESE PLEASE
#python commonset.py apple banana pear grape
#python commonset.py mango mango mango pear grape
#python commonset.py apple banana pear grape mango