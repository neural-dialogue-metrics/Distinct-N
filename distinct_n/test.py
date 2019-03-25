import unittest

from distinct_n import distinct_n_sentence_level
from distinct_n import distinct_n_corpus_level


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

    def test_corpus_level(self):
        sentences = [
            'the cat sat on the mat'.split(),
            'mat the on sat cat the'.split(),
            'i do not know'.split(),
            'Sorry but i do not know'.split(),
        ]
        self.assertAlmostEqual(0.916666, distinct_n_corpus_level(sentences, 1), delta=1e-5)
        self.assertAlmostEqual(0.8125, distinct_n_corpus_level(sentences, 2), delta=1e-5)
