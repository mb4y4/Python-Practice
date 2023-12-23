
# Create a program inrange.py that has a function that takes one integer argument.
# The function will print a list of all values between 3000 and 5000 that is divisible
# by:
# 1. the integer argument
# 2. the integer argument + 7
# 3. the integer argument ^ 2

def print_divisible_values(num):
    # Calculate the values that satisfy the conditions
    values = [i for i in range(3000, 5001) if i % num == 0 or i % (num + 7) == 0 or i % (num ** 2) == 0]

    # Print the list of values
    print(values)

# Example usage:
user_input = int(input("Enter an integer: "))
print_divisible_values(user_input)
