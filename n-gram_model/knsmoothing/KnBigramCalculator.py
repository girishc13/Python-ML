from __future__ import division
from math import log

'''
Bigram calculator uses KN smoothing
'''
__author__ = 'girish'


class KnBigramCalculator(object):
    ABSOLUTE_DISCOUNT = 0.7

    def __init__(self, unigramCalculator):
        self.unigramCalculator = unigramCalculator

    def addTupleToBigramCount(self, bigramTuple):
        if bigramTuple in self.counts:
            self.counts[bigramTuple] += 1
        else:
            self.counts[bigramTuple] = 1

    def calculateBigramCount(self, sentences):
        prevWord = "<s>"
        for sentence in sentences:
            for currWord in sentence:
                if prevWord == "<s>":
                    prevWord = currWord
                    continue
                else:
                    self.addTupleToBigramCount((currWord, prevWord))
                    prevWord = currWord

    def calculate(self, sentences):
        self.counts = {}
        self.calculateBigramCount(sentences)
        self.calculateContinuationProbabilities()
        self.calculateLambdas()

    def calcuateContinuationCounts(self):
        continuationCounts = {}
        for wordTuple in self.counts.keys():
            currWord = wordTuple[0]
            if currWord in continuationCounts:
                continuationCounts[currWord] += 1
            else:
                continuationCounts[currWord] = 1
        return continuationCounts


    def calculatePreceedingCounts(self):
        preceedingCounts = {}
        for wordTuple in self.counts.keys():
            prevWord = wordTuple[1]
            if prevWord in preceedingCounts:
                preceedingCounts[prevWord] += 1
            else:
                preceedingCounts[prevWord] = 1
        return preceedingCounts

    def calculateContinuationProbabilities(self):
        continuationCounts = self.calcuateContinuationCounts()
        self.continuationProbabilities = {}
        numOfWordsPreceedingAllWords = len(self.counts)
        for word, counts in continuationCounts.items():
            self.continuationProbabilities[word] = counts / numOfWordsPreceedingAllWords

    def calculateLambdas(self):
        self.lambdas = {}
        preceedingCounts = self.calculatePreceedingCounts()
        for word, preceedingCount in preceedingCounts.items():
            wordCount = self.unigramCalculator.getCountForWord(word)
            self.lambdas[word] = KnBigramCalculator.ABSOLUTE_DISCOUNT * preceedingCount / wordCount

    def estimateProbability(self, sentences):

        probEst = 0.0
        prevWord = "<s>"
        for sentence in sentences:
            for currWord in sentence:

                if prevWord == "<s>":
                    prevWord = currWord
                    continue
                else:
                    bigramDiscountedProb = self.calculateBigramDiscountedProbability((currWord, prevWord))
                    probEst += log(bigramDiscountedProb)
                    prevWord = currWord

        return probEst

    def calculateBigramDiscountedProbability(self, bigramTuple):
        prevWord = bigramTuple[1]
        currWord = bigramTuple[0]
        prevWordCount = self.unigramCalculator.getCountForWord(prevWord)
        unigramSmoothedProb = self.calculateLambdaForEstimation(prevWord) * self.calculateContinuationProbForEstimate(
            currWord)
        bigramProb = max(
            self.calculateBigramTupleCountForEstimation(bigramTuple) - KnBigramCalculator.ABSOLUTE_DISCOUNT,
            0) / prevWordCount
        return bigramProb + unigramSmoothedProb

    def calculateLambdaForEstimation(self, prevWord):
        if prevWord in self.lambdas.keys():
            return self.lambdas[prevWord]
        else:
            wordCount = self.unigramCalculator.getCountForWord(prevWord)
            return KnBigramCalculator.ABSOLUTE_DISCOUNT / wordCount

    def calculateBigramTupleCountForEstimation(self, bigramTuple):
        if bigramTuple in self.counts.keys():
            return self.counts[bigramTuple]
        else:
            return 0

    def calculateContinuationProbForEstimate(self, currWord):
        if currWord in self.continuationProbabilities.keys():
            return self.continuationProbabilities[currWord]
        else:
            return 1
