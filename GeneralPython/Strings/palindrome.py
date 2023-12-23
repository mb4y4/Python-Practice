def is_palindrome(text):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

    # Check if the cleaned text is a palindrome
    if cleaned_text == cleaned_text[::-1]:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")

# Example usage:
user_input = input("Enter a string: ")
is_palindrome(user_input)
