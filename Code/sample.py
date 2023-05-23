

import random

histogram = [('cats', 3), ('dogs', 4), ('rabbits', 2), ('turtles', 1)]


def sample(histogram):
    """Return a word from this histogram, randomly sampled by weighting"""
    tokens = sum([count for word, count in histogram]) # Count total tokens
    dart = random.randint(1, tokens)

    fence = 0
    for word, count in histogram:
        fence += count
        if fence >= dart:
            return word


def test_sample():
	dad = 0
	mom = 0
	for i in range(10000):
		if sample(histogram) == 'dogs':
			dad += 1
		else:
			mom += 1
	print(dad, mom)

