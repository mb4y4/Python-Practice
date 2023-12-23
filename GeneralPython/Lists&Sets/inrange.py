def print_divisible_values(num):
    # Calculate the values that satisfy the conditions
    values = [i for i in range(3000, 5001) if i % num == 0 or i % (num + 7) == 0 or i % (num ** 2) == 0]

    # Print the list of values
    print(values)

# Example usage:
user_input = int(input("Enter an integer: "))
print_divisible_values(user_input)
