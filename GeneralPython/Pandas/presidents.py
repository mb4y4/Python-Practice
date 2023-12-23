# ● Use the president_heights.csv file to complete the assignment. Create a
# program, presidents.py, that takes two arguments. These arguments will
# correspond to the start and stop of a slice, respectively. It will slice the heights
# column in the president_heights.csv files.
# ● Read in the csv data like so:
# import pandas as pd
# df = pd.read_csv(“president_heights.csv”)
# ● Then print off the average height, rounded to two decimals, of the selected
# presidents in the following form:
# “The average height of presidents number x to y is z”
# Where:
# ● x = start of the slice
# ● y = end of the slice
# ● z = calculated average
# Note: There would be 6 presidents if the “The average height of presidents
# number 4 to 10 is ...” (Think in terms of index slicing when it says 4 to 10)


import pandas as pd
import sys

# Load the CSV data
df = pd.read_csv("president_heights.csv")

def calculate_average_height(start, stop):
    # Slice the heights column based on the provided start and stop indices
    selected_heights = df['height'][start-1:stop]

    # Calculate the average height
    average_height = selected_heights.mean()

    # Print the result
    print(f"The average height of presidents number {start} to {stop} is {average_height:.2f}")

if len(sys.argv) == 3:
    # Example usage:
    # Note: Using int() to convert command-line arguments to integers
    start_index = int(sys.argv[1])
    stop_index = int(sys.argv[2])

    calculate_average_height(start_index, stop_index)
else:
    print("Please provide two indices for the start and stop of the slice.")

#RUN THESE PLEASE
#python presidents.py 4 10
#python presidents.py 1 5