'''
Classifier for classifying reuters documents using DocumentFrequencyCalculator
'''
import os
from WordFreqCalculatorDictTwoClass import WordFreqCalculatorDictTwoClass

from WordFrequencyCalculator import WordFrequencyCalculator
from WordFrequencyCalculatorDict import WordFrequencyCalculatorDict


__author__ = 'girish'


class WordFrequencyClassifier(object):
    def __init__(self):
        # self.calculatorDict = WordFrequencyCalculatorDict()
        self.calculatorDict = WordFreqCalculatorDictTwoClass()

    def train(self):
        self.calculatorDict.train()

    def test(self):
        self.calculatorDict.test()