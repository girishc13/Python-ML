'''
Unigram Calculator dictionary to hold unigram calculators for KN smoothing
'''
import os
from SentenceConstructor import SentenceConstructor

__author__ = 'girish'


class BaseCalculatorDict(object):
    def __init__(self, dataDirectory):
        self.dataDirectory = dataDirectory
        self.calculators = {}

    def calculateFilePath(self, classDir):
        fileName = classDir + "_" + "mega.txt"
        filePath = os.path.abspath(os.path.join(self.dataDirectory, classDir, fileName))
        return filePath

    def constructSentences(self, filePath):
        sentenceConstructor = SentenceConstructor()
        sentences = sentenceConstructor.construct(filePath)
        return sentences

    def calculateForAllDirectories(self):
        # iterate through the directories to build a calculator for each class
        for classDir in os.listdir(self.dataDirectory):
            filePath = self.calculateFilePath(classDir)
            sentences = self.constructSentences(filePath)
            self.calculators[classDir].calculate(sentences)

    def getCalculators(self):
        return self.calculators

    def getCalculatorForClass(self, classDir):
        return self.calculators[classDir]