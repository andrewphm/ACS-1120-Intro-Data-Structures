import sys
import random


def rearrange_words():
    words = sys.argv[1:] # GEt the command-line arguments excluding the script name
    random.shuffle(words) # Randomly rearrange the words
    return ' '.join(words) # Return the shuffled words as a string


if __name__ == '__main__':
    print(rearrange_words())

