from __future__ import division
'''
Base Good-Turing Smoothing Calculator
'''
import collections
from math import log, fabs, sqrt, exp

__author__ = 'girish'


class BaseSmoothingCalculator(object):
    def smoothed(self, i):
        return exp(self.intercept + self.slope * log(i))

    def sq(self, i):
        return i * i

    def row(self, i):
        j = 0

        while (j < self.rows and self.r[j] < i):
            j += 1

        return j if (j < self.rows and self.r[j] == i) else -1

    def calculateSmoothedCount(self, j):
        CONFID_FACTOR = 1.96
        indiffValsSeen = False
        y = (self.r[j] + 1) * self.smoothed(self.r[j] + 1) / self.smoothed(self.r[j])
        if (self.row(self.r[j] + 1) < 0):
            indiffValsSeen = True
        if (not indiffValsSeen):
            next_n = self.n[self.row(self.r[j] + 1)]
            x = (self.r[j] + 1) * next_n / self.n[j]
            if (fabs(x - y) <= CONFID_FACTOR * sqrt(self.sq(self.r[j] + 1.0) \
                    * next_n / (self.sq(self.n[j]))) * (1 + next_n / self.n[j])):
                indiffValsSeen = True
            else:
                return x
        if indiffValsSeen:
            return y

    def calculatePrZero(self):
        bigN = 0.0
        for count, freq in self.Nc.iteritems():
            bigN += count * freq
        # print "bigN : ", bigN
        next_n = self.row(1)
        self.PZero = (0 if next_n < 0 else self.n[next_n]) / bigN
        # print "PZero: ", PZero

    def calculateProbabilities(self):
        self.Nc = {}
        for count in self.counts.values():
            if count in self.Nc:
                self.Nc[count] += 1
            else:
                self.Nc[count] = 1

        # print self.Nc


        # calculateForAllDirectories logr and logZ
        self.Nc = collections.OrderedDict(sorted(self.Nc.items()))
        self.r = self.Nc.keys()
        self.n = self.Nc.values()
        self.rows = len(self.Nc.keys())
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

        self.calculatePrZero()

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
        self.rStar = [None] * self.rows
        for j in range(0, self.rows):
            self.rStar[j] = self.calculateSmoothedCount(j)

            # print "rj: ", self.r
        # print "rStar: ", self.rStar

        # calculateForAllDirectories the final estimated values
        self.bigNPrime = 0.0
        for j in range(0, self.rows):
            self.bigNPrime += self.n[j] * self.rStar[j]
        # print "bigNPrime: ", self.bigNPrime

        self.probabilityEstimatesForCounts = {}
        for j in range(0, self.rows):
            self.probabilityEstimatesForCounts[self.r[j]] = (1 - self.PZero) * self.rStar[j] / self.bigNPrime
            # print "Probabilities: ", self.p
            # print "Probability Sum: ", PZero + sum(self.p)
            # print self.PZero, self.probabilityEstimatesForCounts

    def getSmoothedCount(self, count):
        if count in self.r:
            index = self.r.index(count)
            return self.rStar[index]
        else:
            return self.PZero