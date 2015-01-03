'''
Class to hold all the unigram calculator for a dataset
''' 

import os

from SentenceConstructor import SentenceConstructor
from UnigramCalculator import UnigramCalculator


class UnigramCalculatorDict():
    
    def __init__(self, directory):
        self.calcDirectory = directory
        self.calculators = {}

    def createNewUnigramCalc(self, classDir):
        unigramCalc = UnigramCalculator()
        self.calculators[classDir] = unigramCalc
        return unigramCalc


    def calculateFilePath(self, classDir):
        fileName = classDir + "_" + "mega.txt"
        filePath = os.path.abspath(os.path.join(self.calcDirectory, classDir, fileName))
        return filePath


    def constructSentences(self, filePath):
        sentenceConstructor = SentenceConstructor()
        sentences = sentenceConstructor.construct(filePath)
        return sentences

    def calculateForAllDirectories(self):
        # iterate through the directories to build a calculator for each class
        for classDir in os.listdir(self.calcDirectory):
            unigramCalc = self.createNewUnigramCalc(classDir)
            filePath = self.calculateFilePath(classDir)
            sentences = self.constructSentences(filePath)
            unigramCalc.calculate(sentences)
    
    def getCalculators(self):
        return self.calculators

    def getCalculatorForClass(self, classDir):
        return self.calculators[classDir]