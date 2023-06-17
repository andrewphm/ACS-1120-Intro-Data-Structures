import re
import random
from collections import defaultdict
from dictogram import Dictogram

class MarkovChain:
    def __init__(self, text=None):
        # Initialize a dictionary with Dictogram as the default value factory
        self.chain = defaultdict(Dictogram)
        if text:
            self.train(text)

    def train(self, text):
        # Preprocess the text and split it into words
        words = self.preprocess_text(text)
        # For each pair of words, update the Dictogram of words that can follow the first word
        if words:
            for i in range(len(words) - 1):
                self.chain[words[i]].add_count(words[i + 1])

    def generate_sentence(self, length=10):
        # If length is less than 1 or chain is empty, return an empty string
        if length < 1 or not self.chain:
            return ""
        # Start with a random word from the keys of the chain
        start_word = random.choice(list(self.chain.keys()))
        sentence = [start_word]
        # Generate the rest of the sentence
        for _ in range(length - 1):
            sentence.append(self.chain[sentence[-1]].sample())
        return ' '.join(sentence)

    @staticmethod
    def preprocess_text(text):
        # Remove punctuation and split the text into words
        text = MarkovChain.remove_punctuation(text)
        return MarkovChain.split_into_words(text)

    @staticmethod
    def remove_punctuation(text):
        # Replace punctuation with spaces
        return re.sub(r'[.!?]+', ' ', text)

    @staticmethod
    def split_into_words(text):
        # Remove non-alphabetic characters and split the text into words
        return re.sub(r'[^a-zA-Z\’\'\s]+', ' ', text).split()

def main():

    text = """
    Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'
    So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.
    There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, 'Oh dear! Oh dear! I shall be late!' (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge.
    """

    markov = MarkovChain(text)
    print(markov.generate_sentence(20))

if __name__ == '__main__':
    main()
