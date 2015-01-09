'''
Class for performing unigram calculations for spelling correction task
'''
import os
import re
from DamerauLevenshteinDistanceCalculator import DamerauLevenshteinDistanceCalculator


__author__ = 'girish'


class UnigramCalculator(object):
    REGEX_PUNCTUATION = r'\?|\!\s|\?\$|\!$|\.\s|\.$|\,|\:'

    def __init__(self):
        self.dlDistCalculator = DamerauLevenshteinDistanceCalculator()

    def updateWordCount(self, word):
        if word in self.counts:
            self.counts[word] += 1
        else:
            self.counts[word] = 1

    def stripTokenOfPunctuations(self, token):
        matchPunct = re.search(UnigramCalculator.REGEX_PUNCTUATION, token, re.MULTILINE)
        if matchPunct:
            searchPunct = re.search(UnigramCalculator.REGEX_PUNCTUATION, token)
            word = searchPunct.string[0:searchPunct.start(0)]
        else:
            word = token
        return word

    def processToken(self, token):
        word = self.stripTokenOfPunctuations(token)
        word = word.lower()
        return word


    def getDataFromFile(self, classDir, dataDir):
        fileName = classDir + "_" + "mega.txt"
        textFile = open(os.path.join(dataDir, classDir, fileName), "r")
        data = textFile.read()
        return data

    def getSentencesFromFile(self, classDir, dataDir):
        data = self.getDataFromFile(classDir, dataDir)
        sentences = re.split(r'( *[\.])', data)
        return sentences

    def calculateCounts(self, dataDir):
        self.counts = {}
        self.totalWordCount = 0.0
        for classDir in os.listdir(dataDir):
            sentences = self.getSentencesFromFile(classDir, dataDir)
            for sentence in sentences:
                for token in sentence.split():
                    if token == ".":
                        continue
                    word = self.processToken(token)
                    self.totalWordCount += 1
                    self.updateWordCount(word)

    def calculateProbabilities(self):
        self.probabilities = {}
        for word, count in self.counts.items():
            self.probabilities[word] = count / self.totalWordCount

    def calculate(self, dataDir):
        self.calculateCounts(dataDir)
        self.calculateProbabilities()

    def getCandidateList(self, candidateWord):
        candidateList = []
        for word in self.counts.keys():
            distance = self.dlDistCalculator.calculateDistance(candidateWord, word)
            if distance == 1 :
                candidateList.append((word, self.probabilities[word]))
        return candidateList
