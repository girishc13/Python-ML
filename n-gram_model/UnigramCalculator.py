from __future__ import  division
__author__ = 'girish'
# Perform Unigram Calculations for Good-Turing smoothing

import collections
from math import log
from math import exp
from math import fabs
from math import sqrt

class UnigramCalculator():

    def __init__(self):
        pass

    def smoothed(self, i):
        return exp(self.intercept + self.slope * log(i))

    def sq(self, i):
        return i * i

    def row(self, i):
        j = 0

        while(j < self.rows and self.r[j] < i):
            j += 1

        return j if (j < self.rows and self.r[j] == i) else -1

    def calculateForAllDirectories(self, sentences):
        self.unigramCount = {}
        self.totalWord = 0
        self.Nc = {}

        for sentence in sentences:

            for token in sentence:
                if token in self.unigramCount:
                    self.unigramCount[token] += 1
                else:
                    self.unigramCount[token] = 1

                self.totalWord += 1

        # calculateForAllDirectories frequency of frequencies
        for count in self.unigramCount.values():
            if count in self.Nc:
                self.Nc[count] += 1
            else:
                self.Nc[count] = 1

        # print self.Nc

        bigN = 0.0
        self.rows = len(self.Nc.keys())
        for count, freq in self.Nc.iteritems():
                bigN += count * freq

        # print "bigN : ", bigN
        next_n = self.Nc.keys()[1]
        self.PZero = (0 if next_n < 0 else self.Nc[next_n]) / bigN
        # print "PZero: ", PZero

        # calculateForAllDirectories logr and logZ
        self.Nc = collections.OrderedDict(sorted(self.Nc.items()))
        self.r = self.Nc.keys()
        self.n = self.Nc.values()
        Z = [None] * self.rows
        log_r = [None] * self.rows
        log_Z = [None] * self.rows
        for j in range(0, self.rows):
            i = 0 if j == 0 else self.r[j - 1]
            if j == self.rows - 1:
                k = 2 * self.r[j] - i
            else:
                k = self.r[j + 1]
            Z[j] = 2 * self.n[j] / (k - i)
            log_r[j] = log(self.r[j])
            log_Z[j] = log(Z[j])

        # calculateForAllDirectories the best fit params
        XYs = Xsquares = meanX = meanY = 0.0
        for i in range(0, self.rows):
            meanX += log_r[i]
            meanY += log_Z[i]

        meanX /= self.rows
        meanY /= self.rows
        for i in range(0, self.rows):
            XYs += (log_r[i] - meanX) * (log_Z[i] - meanY)
            Xsquares += self.sq(log_r[i] - meanX)

        self.slope = XYs / Xsquares
        self.intercept = meanY - self.slope * meanX

        # calculateForAllDirectories new estimated counts
        indiffValsSeen = False
        CONFID_FACTOR = 1.96
        self.rStar = [None] * self.rows
        for j in range(0, self.rows):
            y = (self.r[j] + 1) * self.smoothed(self.r[j] + 1) / self.smoothed(self.r[j])
            if (self.row(self.r[j] + 1) < 0):
                indiffValsSeen = True

            if(not indiffValsSeen):
                next_n = self.n[self.row(self.r[j] + 1)]
                x = (self.r[j] + 1) * next_n / self.n[j]
                if(fabs(x - y) <= CONFID_FACTOR * sqrt(self.sq(self.r[j] + 1.0) \
                        * next_n / (self.sq(self.n[j]))) * (1 + next_n / self.n[j])):
                    indiffValsSeen = True
                else:
                    self.rStar[j] = x

            if indiffValsSeen:
                self.rStar[j] = y
        # print "rj: ", self.r
        # print "rStar: ", self.rStar

        # calculateForAllDirectories the final estimated values
        self.bigNPrime = 0.0
        for j in range(0, self.rows):
            self.bigNPrime += self.n[j] * self.rStar[j]
        # print "bigNPrime: ", self.bigNPrime

        self.p = [None] * self.rows
        for j in range(0, self.rows):
            self.p[j] = (1 - self.PZero) * self.rStar[j] / self.bigNPrime
        # print "Probabilities: ", self.p
        # print "Probability Sum: ", PZero + sum(self.p)

        # construct dictionary of counts and probabilities
        self.UnigramEst = {}
        for j in range(0, self.rows):
            self.UnigramEst[self.r[j]] = self.p[j]

    def getUnigramCount(self):
        return self.unigramCount

    def getNc(self):
        return self.Nc

    def predict(self, sentences):

        probEst = 0.0
        for sentence in sentences:
            for token in sentence:
                if token in self.unigramCount:
                    count = self.unigramCount[token]
                    probEst += log(self.UnigramEst[count])
                    # probEst *= self.UnigramEst[count]
                else:
                    probEst += log(self.PZero)
                    # probEst *= self.PZero

        return probEst
