import sys
import random
import os

def generate_random_sentence():
    if len(sys.argv) < 2:
        print('You didn\'t provide a number of words. Please enter a number')
        num_words = int(input())
    else:
        num_words = int(sys.argv[1])

    """"
    # Open the file in read mode
    with open('/usr/share/dict/words', 'r') as f:
        # Read the contents of the file into memory
        words = f.read()
        # Split the text into words based on whitespace
        words = words.split()
        # Choose one of the words at random
        random_word = random.choice(words)
        # Print the random word
        print(random_word)
    """

    # Open the file in read mode
    with open('/usr/share/dict/words', 'r') as f:
        # Read the contents of the file into memory
        words = f.read().splitlines()
        # Choose one of the words at random
        random_words = random.choices(words, k=num_words)
        # Print the random word
        sentence = ' '.join(random_words)
        return sentence

if __name__ == '__main__':
    print(generate_random_sentence())
