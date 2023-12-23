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