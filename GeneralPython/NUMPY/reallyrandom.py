
# ● Create a program called reallyrandom.py that has a function that takes in three
# arguments and prints one integer. Set your numpy random seed to 42.
# ○ The first argument should correspond to the size of a np.randint that has
# values from 0 to 10.
# ○ The second is an integer that you will multiply the randint by.
# ○ The third argument is a value you will index the result of the multiplication
# by.
# ● The program should not crash if the third value is larger than the first.
# ● You will print the integer that was indexed as ‘Your random value is x’ where x =
# the result of the indexing.

import numpy as np

def generate_random_value(size, multiplier, index_value):
    # Set numpy random seed to 42
    np.random.seed(42)

    # Generate random integers
    random_integers = np.random.randint(0, 10, size=size)

    # Multiply by the second argument
    multiplied_values = random_integers * multiplier

    try:
        # Index the result
        indexed_value = multiplied_values[index_value]
        print(f'Your random value is {indexed_value}')
    except IndexError:
        print('Index is out of bounds. Provide a valid index.')

# Example usage:
generate_random_value(5, 3, 2)
