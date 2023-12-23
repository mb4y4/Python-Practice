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
