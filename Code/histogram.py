import string
from collections import Counter
import timeit



def histogram(source_text):
    with open(source_text, 'r') as f:
        text = f.read()

        # remove punctuation and numbers
        translator = str.maketrans('', '', string.punctuation + string.digits)
        text = text.translate(translator)

        words = text.lower().split()
        histogram = {}

        for word in words:
            if word not in histogram:
                histogram[word] = 1
            else:
                histogram[word] += 1

        return histogram

def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    word = word.lower()
    return histogram.get(word, 0)


if __name__ == '__main__':

    # Measure execution time using timeit
    execution_time = timeit.timeit(lambda: histogram('data/paragraph.txt'), number=1)

    hist = histogram('data/paragraph.txt')
    print("Number of unique words: ", unique_words(hist))
    print("Frequency of 'the': ", frequency('the', hist))

    # Print the execution time
    print(f"Execution Time: {execution_time} seconds")







