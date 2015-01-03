'''
Bigram calculator class uses good-turing smoothing for a single class
'''
from math import log

__author__ = 'girish'
from BaseSmoothingCalculator import BaseSmoothingCalculator


class BigramCalculator(BaseSmoothingCalculator):

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
        self.calculateProbabilities()

    def estimateProbability(self, sentences):

        probEst = 0.0
        prevWord = "<s>"
        for sentence in sentences:
            for currWord in sentence:

                if prevWord == "<s>":
                    prevWord = currWord
                    continue
                else:
                    bigramTuple = (currWord, prevWord)
                    prevWord = currWord
                    if bigramTuple in self.counts:
                        count = self.counts[bigramTuple]
                        probEst += log(self.probabilityEstimatesForCounts[count])
                        # probEst *= self.UnigramEst[count]
                    else:
                        probEst += log(self.PZero)
                    #     # probEst *= self.PZero

        return probEst
