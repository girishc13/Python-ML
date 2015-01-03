'''
Trigram calculator class uses good-turing smoothing for a single class
'''

from math import log
from BaseSmoothingCalculator import BaseSmoothingCalculator

__author__ = 'girish'


class TrigramCalculator(BaseSmoothingCalculator):

        def updatePrevTuple(self, currWord, prevTuple):
            preceedingWord = prevTuple[0]
            prevTuple = (currWord, preceedingWord)
            return prevTuple

        def addTrigramTupleToCounts(self, currWord, prevTuple):
            trigramTuple = (currWord, prevTuple)
            if trigramTuple in self.counts:
                self.counts[trigramTuple] += 1
            else:
                self.counts[trigramTuple] = 1

        def calculateTrigramCounts(self, sentences):
            prevTuple = ("<s>", "<s>")
            for sentence in sentences:
                for currWord in sentence:
                    if prevTuple[0] == "<s>":
                        prevTuple = (currWord, "<s>")
                    elif prevTuple[1] == "<s>":
                        prevTuple = self.updatePrevTuple(currWord, prevTuple)
                    else:
                        self.addTrigramTupleToCounts(currWord, prevTuple)
                        prevTuple = self.updatePrevTuple(currWord, prevTuple)

        def calculate(self, sentences):
            self.counts = {}
            self.calculateTrigramCounts(sentences)
            self.calculateProbabilities()

        def estimateProbability(self, sentences):
            probEst = 0.0
            prevTuple = ("<s>", "<s>")
            for sentence in sentences:
                for currWord in sentence:
                    if prevTuple[0] == "<s>":
                        prevTuple = (currWord, "<s>")
                    elif prevTuple[1] == "<s>":
                        prevTuple = self.updatePrevTuple(currWord, prevTuple)
                    else:
                        trigramTuple = (currWord, prevTuple)
                        prevTuple = self.updatePrevTuple(currWord, prevTuple)
                        if trigramTuple in self.counts:
                            count = self.counts[trigramTuple]
                            probEst += log(self.probabilityEstimatesForCounts[count])
                        else:
                            probEst += log(self.PZero)

            return probEst