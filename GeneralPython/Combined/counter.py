
# Create a program, counter.py. You are given a single string argument. Print a
# dictionary where the keys are composed of each letter from a word and values
# are the sum of each letters’ appearances. The key order should be in the order of
# the letters’ appearances.

import sys

# Load variable from command-line argument
word = sys.argv[1]

# Create a dictionary to store letter frequencies
letter_counts = {}

# Count the occurrences of each letter in the word
for letter in word:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

# Print the resulting dictionary
print(letter_counts)

#RUN THESE PLEASE
#python counter.py good
#python counter.py Mississippi
#python counter.py onomatopoeia