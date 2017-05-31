#! /usr/bin/python3
"""Generate Markov Dataset script."""
import re
import sys

from nltk.corpus import wordnet as wn
from collections import defaultdict


def __clean__(word):
	"""Simply remove all trash characters."""
	return re.sub('[^A-Za-z0-9]+', '', word)


if __name__ == "__main__":    
	lang = sys.argv[1]
	freqs = defaultdict(lambda: 0)
	counter = 0
	for word in wn.words(lang):
		word = __clean__(word.lower())
		if len(word) > 0:
			counter += 1
			if len(word) < 3:
				freqs[word] += 1
			else:
				freqs[word[:3]] += 1
	for word in freqs:
		print("{},{}".format(word, freqs[word]/counter))