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