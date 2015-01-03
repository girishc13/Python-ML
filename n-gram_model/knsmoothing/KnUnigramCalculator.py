'''
Unigram calculator for KN smoothing
'''
from gtsmoothing.UnigramCalculator import UnigramCalculator

__author__ = 'girish'

class KnUnigramCalculator(UnigramCalculator):

    ABSOLUTE_DISCOUNT = 0.7

    def __init__(self):
        super(KnUnigramCalculator, self).__init__()
        
    def calculate(self, sentences):
        super(KnUnigramCalculator, self).calculate(sentences)

    def getAllWords(self):
        return self.counts.keys()
