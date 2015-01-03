'''
Bigram calculator dictionary to hold all bigram calculators for KN smoothing
'''
import os

from BaseCalculatorDict import BaseCalculatorDict
from KnBigramCalculator import KnBigramCalculator


__author__ = 'girish'


class BigramCalculatorDict(BaseCalculatorDict):
    def createCalculators(self):
        for classDir in os.listdir(self.dataDirectory):
            self.calculators[classDir] = KnBigramCalculator(self.unigramCalculatorDict.getCalculatorForClass(classDir))

    def __init__(self, dataDirectory, unigramCalculatorDict):
        super(BigramCalculatorDict, self).__init__(dataDirectory)
        self.unigramCalculatorDict = unigramCalculatorDict
        self.createCalculators()
