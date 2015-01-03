'''
Unigram calculator dictionary to hold all unigram calculators for KN smoothing
'''
import os
from BaseCalculatorDict import BaseCalculatorDict
from KnUnigramCalculator import KnUnigramCalculator


__author__ = 'girish'

class UnigramCalculatorDict(BaseCalculatorDict):

    def createCalculators(self):
        for classDir in os.listdir(self.dataDirectory):
            self.calculators[classDir] = KnUnigramCalculator()

    def __init__(self, dataDirectory):
        super(UnigramCalculatorDict, self).__init__(dataDirectory)
        self.createCalculators()