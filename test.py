from unittest import TestCase
import distinct_metric
import unittest


class TestDistinctN(unittest.TestCase):
    def test_unigram(self):
        sentence = "the the the the the"
        self.assertAlmostEqual(
            distinct_metric.compute_distinct_metric(sentence, 1), 0.2
        )
        sentence = "the the the the cat"
        self.assertAlmostEqual(
            distinct_metric.compute_distinct_metric(sentence, 1), 0.4
        )

    def test_bigram(self):
        sentence = "the cat sat on the"
        self.assertAlmostEqual(
            distinct_metric.compute_distinct_metric(sentence, 2), 0.8
        )


if __name__ == '__main__':
    unittest.main()
