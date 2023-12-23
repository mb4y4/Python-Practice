import sys

# Load variables from command-line arguments
loop_list = sys.argv[1:]

# Convert string-type integers to integer-type and add their own index positions
result = [int(num) + index for index, num in enumerate(loop_list)]

# Print the output
print(result)

#RUN THESE PLEASE
#python loopindex.py 5 5 5
#python loopindex.py 1 2 3 4 5
#python loopindex.py 4 11 0 0 1
