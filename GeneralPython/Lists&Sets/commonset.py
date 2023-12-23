
# For this assignment, load in your variables like this:
# set_a = sys.argv[1:]
# set_b = ['apple', 'banana', 'mango', 'orange']
# b. The above set_a is a list-type variable which contains words.
# c. Your order may be different for the examples below because sets are
# unordered.

# ● Create a program, commonset.py. Your program should:
# a. Find the common words between set_a and set_b.
# b. Print the output in a set format.

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