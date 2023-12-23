
# For this assignment, load in your sys.argv like so:
# duplicated_words = sys.argv[1:]
# The above duplicated_words is a list-type variable which contains a whole
# bunch of lower-cased words (ex. ['hello', 'world', 'welcome', 'hello', 'again']).

# ● Create a program, duplicates.py. It should:
# a. Remove all duplicate words from the list
# b. Then print it in descending order of alphabets (from Z to A).


import sys

# Load variable from command-line argument
duplicated_words = sys.argv[1:]

# Remove duplicate words and sort in descending order
unique_sorted_list = sorted(set(duplicated_words), reverse=True)

# Print the result
print(unique_sorted_list)

#RUN THESE PLEASE
#python duplicates.py hello world welcome hello again
#python duplicates.py hello world welcome hello again hello
#python duplicates.py apple banana apple orange pear banana
#python duplicates.py apple banana apple orange pear banana banana banana