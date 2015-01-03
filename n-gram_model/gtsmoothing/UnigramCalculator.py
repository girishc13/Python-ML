from __future__ import division

import collections
from math import exp, log, fabs, sqrt
from math import fabs
from math import log
from math import sqrt
from BaseSmoothingCalculator import BaseSmoothingCalculator

__author__ = 'girish'
# Perform Unigram Calculations for Good-Turing smoothing for a single class

class UnigramCalculator(BaseSmoothingCalculator):

    def calculate(self, sentences):
        self.counts = {}

        for sentence in sentences:
            for token in sentence:
                if token in self.counts:
                    self.counts[token] += 1
                else:
                    self.counts[token] = 1

        self.calculateProbabilities()


    def estimateProbability(self, sentences):

        probEst = 0.0
        for sentence in sentences:
            for token in sentence:
                if token in self.counts:
                    count = self.counts[token]
                    probEst += log(self.probabilityEstimatesForCounts[count])
                    # probEst *= self.UnigramEst[count]
                else:
                    probEst += log(self.PZero)
                    # probEst *= self.PZero

        return probEst