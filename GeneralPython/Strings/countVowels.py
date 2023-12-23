
# ● Create a program called countVowels.py that has a function that takes in a string
# then prints the number of unique vowels in the string (regardless of it being upper
# or lower case).


def count_unique_vowels(input_string):
    # Convert the input string to lowercase to make the comparison case-insensitive
    input_string = input_string.lower()

    # Define the set of vowels
    vowels = set("aeiou")

    # Initialize a set to store unique vowels found in the input string
    unique_vowels = set()

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a vowel
        if char in vowels:
            # Add the lowercase version of the vowel to the set
            unique_vowels.add(char)

    # Print the number of unique vowels found
    print(f"Number of unique vowels: {len(unique_vowels)}")

# Prompt the user to input a string
user_input = input("Enter a string: ")

# Call the function with the user's input
count_unique_vowels(user_input)
