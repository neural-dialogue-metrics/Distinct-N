# MIT License
# 
# Copyright (c) 2019 Cong Feng.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
