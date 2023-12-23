
# Create a program called arrayargs.py that has a function that takes four integer
# arguments. Those arguments should be put into an Numpy array.
# ● The function will have two print statements.
# ○ The first will print the type of the array you create (which should be <class
# ‘numpy.ndarray’>).
# ■ For this, DO NOT just do print(“<class ‘numpy.ndarray’>”)
# ○ The second will print the multiplication of the four items in your array.


import numpy as np
import sys

def process_array_args(arg1, arg2, arg3, arg4):
    # Create a NumPy array from the arguments
    my_array = np.array([arg1, arg2, arg3, arg4])

    # Print the type of the array
    print(type(my_array))

    # Print the multiplication of the four items in the array
    print(np.prod(my_array))

# Example usage:
# Note: Using int() to convert command-line arguments to integers
process_array_args(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))

#RUN THESE PLEASE
#python arrayargs.py 2 4 5 2
#python arrayargs.py 3 6 9 12
