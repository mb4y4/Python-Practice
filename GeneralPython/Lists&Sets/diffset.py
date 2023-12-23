
# For this assignment, load in your variables like this:
# set_a = sys.argv[1:]
# set_b = ['apple', 'banana', 'mango', 'orange']
# b. The above set_a is a list-type variable which contains words.
# c. Your order may be different for the examples below because sets are
# unordered.

# ● Create a program, diffset.py. Your program should:
# a. Find the words that exists in set_a but are not in set_b.
# b. Print the output in a set format.

import sys

# Load variables from command-line arguments
set_a = set(sys.argv[1:])
set_b = {'apple', 'banana', 'mango', 'orange'}  # Using a set for set_b

# Find words that exist in set_a but are not in set_b
difference_words = set_a.difference(set_b)

# Print the output in a set format
print(difference_words)

#RUN THESE PLEASE
#python diffset.py apple cherry
#python diffset.py mango mango mango pear grape