
# For this assignment, load in your sys.argv like so:
# my_ints = sys.argv[1:]
# ○ The above my_ints a list-type variable which contain numbers that are
# string-typed (ex. ['1', '2', '3', '4', '5'])

# ● Create a program, comprehension.py. Your program should:
# 1. Convert these string-type integers into integer-type.
# 2. If the number within the list is divisible by 3, multiply it by 10, then replace
# it.


import sys

# Load variables from command-line arguments
my_ints = sys.argv[1:]

# Convert string-type integers to integer-type and apply the condition
result = [int(num) * 10 if int(num) % 3 == 0 else int(num) for num in my_ints]

# Print the output
print(result)

#RUN THESE PLEASE
#python comprehension.py 1 2 3 4 5
#python comprehension.py 3 6 9 12 15
#python comprehension.py 3 30 1 15 10
