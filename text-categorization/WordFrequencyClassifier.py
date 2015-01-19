'''
Classifier for classifying reuters documents using DocumentFrequencyCalculator
'''
import os

from WordFrequencyCalculator import WordFrequencyCalculator
from WordFrequencyCalculatorDict import WordFrequencyCalculatorDict


__author__ = 'girish'


class WordFrequencyClassifier(object):
    def __init__(self):
        self.calculatorDict = WordFrequencyCalculatorDict()

    def train(self):
        self.calculatorDict.train()

    def test(self):
        self.calculatorDict.test()