def shortest_word(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Find the shortest word
    shortest = min(words, key=len)

    # Print the result
    print(f"The shortest word is {shortest.upper()}")

# Example usage:
user_input = input("Enter a sentence: ")
shortest_word(user_input)
