
# ● Create a program, shortest.py, that has a function that takes in a string argument
# and prints a sentence indicating the shortest word in that string. If there is more
# than one word print only the first. 

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
