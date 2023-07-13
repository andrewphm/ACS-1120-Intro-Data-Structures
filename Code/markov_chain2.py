import random
import re
from typing import List, Tuple

class MarkovGenerator:
    def __init__(self, order: int = 2) -> None:
        self.words_histogram = {}
        self.order = order

    def read_file(self, file_name: str) -> List[str]:
        """
        Reads given source file and returns list of words
        """
        with open(file_name) as f:
            text = f.read()
            text = text.replace("’", "'")
            text_without_numbers = re.sub(r"\d+", "", text)  # Remove all numbers from the text
            words = [match.group() for match in re.finditer(r"[a-zA-Z0-9_'.:,-;!?]+", text_without_numbers)]
        return words

    def prepare_histogram(self, file_name: str) -> None:
        """
        Reads given source file, creates a Dictogram and stores it in self.words_histogram
        """
        words = self.read_file(file_name)
        for i in range(len(words) - self.order):
            sequence = tuple(words[i:i+self.order])
            if sequence not in self.words_histogram:
                self.words_histogram[sequence] = []
            self.words_histogram[sequence].append(words[i+self.order])

    def generate_lyrics(self, number: int = 50) -> str:
        """
        Generates a random song lyrics from the given text and word count number.
        """

        start_sequence = random.choice(list(self.words_histogram.keys()))
        lyrics = list(start_sequence)

        for _ in range(number):
            lyrics.append(random.choice(self.words_histogram[tuple(lyrics[-self.order:])]))

        return ' '.join(lyrics)

if __name__ == "__main__":
    generator = MarkovGenerator(order=2)
    generator.prepare_histogram("lyrics.txt")
    try:
        generated_lyrics = generator.generate_lyrics(50)
        print(generated_lyrics)
    except Exception as e:
        print(e)
