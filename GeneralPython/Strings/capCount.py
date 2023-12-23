def count_capitals(string):
    # Initialize variables to store the count and sum of indices
    count = 0
    index_sum = 0

    # Iterate through each character and its index in the string
    for index, char in enumerate(string):
        # Check if the character is a capital letter
        if char.isupper():
            # Increment the count of capital letters
            count += 1
            # Add the index to the sum of indices
            index_sum += index

    # Print the number of capital letters
    print(count)

    # Print the sum of indices of capital letters
    print(index_sum)

# Example usage:
count_capitals("hEllo, World")  # Should print:
# 2 (number of capital letters)
# 8 (sum of indices of capital letters)
