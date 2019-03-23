from unittest import TestCase
from distinct_n import distinct_n_sentence_level
import unittest


class TestDistinctN(unittest.TestCase):
    def test_unigram(self):
        sentence = "the the the the the".split()
        self.assertAlmostEqual(
            distinct_n_sentence_level(sentence, 1), 0.2
        )
        sentence = "the the the the cat".split()
        self.assertAlmostEqual(
            distinct_n_sentence_level(sentence, 1), 0.4
        )

    def test_bigram(self):
        sentence = "the cat sat on the".split()
        self.assertAlmostEqual(
            distinct_n_sentence_level(sentence, 2), 0.8
        )
