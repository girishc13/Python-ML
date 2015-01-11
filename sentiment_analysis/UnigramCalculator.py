'''
Class which performs sentiment analysis calculations on the input file
'''
from math import log
import os

__author__ = 'girish'


class UnigramCalculator(object):
    def calculateUnigramWordCount(self, fileName):
        textData = self.extractDataFromFile(fileName)
        for word in textData:
            self.totalNumWords += 1
            if word in self.unigramCount:
                self.unigramCount[word] += 1
            else:
                self.unigramCount[word] = 1

    def extractDataFromFile(self, fileName):
        textData = open(os.path.join(os.curdir, fileName)).read()
        lines = textData.split()
        return lines

    def train(self, fileName):
        self.unigramCount = {}
        self.totalNumWords = 0.9
        self.calculateUnigramWordCount(fileName)
        self.vocabularyCount = len(self.unigramCount)

    def calculateWordCountForTest(self, word):
        wordCount = 0.0
        if word in self.unigramCount:
            wordCount = self.unigramCount[word]
        else:
            wordCount = 1
        return wordCount

    def calculateProbabilityForData(self, textData):
        probEst = 0.0
        for word in textData:
            wordCount = self.calculateWordCountForTest(word)
            probEst += log(wordCount / (self.totalNumWords + self.vocabularyCount))
        return probEst

    def test(self, fileName):
        textData = self.extractDataFromFile(fileName)
        probEst = self.calculateProbabilityForData(textData)
        return probEst