def luke_relationship(character):
    # The given dictionary
    relations = {'Darth Vader': 'father', 'Leia': 'sister', 'Han': 'brother in law',
                 'R2D2': 'droid', 'Rey': 'Padawan', 'Tatooine': 'homeworld'}

    try:
        # Special case for Darth Vader
        relationship = relations.get(character, "This character is not in the relations dictionary.")
        if character == 'Darth Vader':
            print("No, I am your", relationship)
        else:
            # Print the general relationship statement
            print(f"Luke, I am your {relationship}")
    except:
        print("An error occurred.")

# Example usage:
user_input = input("Enter a character: ")
luke_relationship(user_input)
