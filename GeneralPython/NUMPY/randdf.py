
# Create a program called randdf.py that has a function that takes two integer
# arguments and prints a Pandas dataframe. The two arguments will correspond
# to the number of rows and number of columns, respectively. The dataframe
# should be filled with random integers from 0 to 100.
# ● Set your numpy random seed to 56.
# ○ Note: Use random from numpy. Otherwise, you might get a different result.


import numpy as np
import sys

def generate_random_array(num_rows, num_columns):
    # Set numpy random seed to 56
    np.random.seed(56)

    # Create a NumPy array with random integers
    rand_array = np.random.randint(0, 101, size=(num_rows, num_columns))

    # Print the array
    print(rand_array)

# Example usage:
# Note: Using int() to convert command-line arguments to integers
generate_random_array(int(sys.argv[1]), int(sys.argv[2]))



#RUN THESE PLEASE
#python randdf.py 3 4
#python randdf.py 5 6