'''
Classifier for classifying reuters documents using DocumentFrequencyCalculator
'''
import os

from DocumentFrequencyCalculator import DocumentFrequencyCalculator
from DocumentFrequencyCalculatorDict import DocumentFrequencyCalculatorDict


__author__ = 'girish'


class DocumentFrequencyClassifier(object):
    def __init__(self):
        self.calculatorDict = DocumentFrequencyCalculatorDict()

    def train(self):
        self.calculatorDict.train()

    def test(self):
        self.calculatorDict.test()