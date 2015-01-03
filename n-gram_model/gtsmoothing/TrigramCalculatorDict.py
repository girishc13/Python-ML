'''
Class to hold all the trigram calculators for a dataset
'''
import os

from SentenceConstructor import SentenceConstructor
from TrigramCalculator import TrigramCalculator


__author__ = 'girish'


class TrigramCalculatorDict():
    def __init__(self, directory):
        self.dataDirectory = directory
        self.calculators = {}

    def createNewTrigramCalculator(self, classDir):
        trigramCalc = TrigramCalculator()
        self.calculators[classDir] = trigramCalc
        return trigramCalc

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
            trigramCalc = self.createNewTrigramCalculator(classDir)
            filePath = self.calculateFilePath(classDir)
            sentences = self.constructSentences(filePath)
            trigramCalc.calculate(sentences)

    def getCalculators(self):
        return self.calculators

    def getCalculatorForClass(self, classDir):
        return self.calculators[classDir]