'''
Class to hold all the bigram calculators for a dataset
'''
from SentenceConstructor import SentenceConstructor

__author__ = 'girish'
import os

from BigramCalculator import BigramCalculator


class BigramCalculatorDict():
    def __init__(self, directory):
        self.dataDirectory = directory
        self.calculators = {}

    def createNewBigramCalculator(self, classDir):
        bigramCalc = BigramCalculator()
        self.calculators[classDir] = bigramCalc
        return bigramCalc

    def calculateFilePath(self, classDir):
        fileName = classDir + "_" + "mega.txt"
        filePath = os.path.abspath(os.path.join(self.dataDirectory, classDir, fileName))
        return filePath

    def constructSentences(self, filePath):
        sentenceConstructor = SentenceConstructor()
        sentences = sentenceConstructor.construct(filePath)
        return sentences

    def calculateForAllDirectories(self):
        for classDir in os.listdir(self.dataDirectory):
            bigramCalc = self.createNewBigramCalculator(classDir)
            filePath = self.calculateFilePath(classDir)
            sentences = self.constructSentences(filePath)
            bigramCalc.calculate(sentences)

    def getCalculators(self):
        return self.calculators

    def getCalculatorForClass(self, classDir):
        return self.calculators[classDir]