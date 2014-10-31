from __future__ import division
__author__ = 'girish'

# Trigram Model MLE probability calculator and estimator

import re
import operator

class TrigramMLE():

    def __init__(self, textFileName):
        self.textFileName = textFileName
        self.trigramEst = {}
        self.trigramCount = {}

    # calculates the trigram model training parameters
    def calculate(self, bigramCount):
        textFile = open(self.textFileName, "r")
        data = textFile.read()
        sentences = re.split(r'( *[\.])', data)

        # do trigram counting of words
        prevTuple = ("<s>", "<s>")
        for sentence in sentences:

            for word in sentence.split():
                if word == ".":
                    word = "<s>"

                trigramTuple = (word, prevTuple)

                # count the trigram
                if trigramTuple in self.trigramCount:
                    self.trigramCount[trigramTuple] += 1
                else:
                    self.trigramCount[trigramTuple] = 1

                preceedingWord = prevTuple[0]
                prevTuple = (word, preceedingWord)

        # print self.trigramCount

        # calculate probalities using the count
        for gram, count in self.trigramCount.iteritems():
            preceedingTuple = gram[1]
            if bigramCount.has_key(preceedingTuple):
                self.trigramEst[gram] = self.trigramCount[gram] / bigramCount[preceedingTuple]

        # print calculated probability
        # for gram, prob in self.trigramEst.iteritems():
        #     print gram, prob

    # Returns the trigram calculations for initialized text
    def getTrigramEst(self):
        return self.trigramEst

    # Returns the trigram count
    def getTrigramCount(self):
        return self.trigramCount

    # estimates the probability of the input text from the calculated estimates
    def estimateProbability(self, textFileName):
        textFile = open(textFileName, "r")
        data = textFile.read()
        sentences = re.split(r'( *[\.])', data)
        probability = 1.0

        prevTuple = ("<s>", "<s>")
        for sentence in sentences:

            for word in sentence.split():
                if word == ".":
                    word = "<s>"

                trigramTuple = (word, prevTuple)

                if self.trigramEst.has_key(trigramTuple):
                    probability *= self.trigramEst[trigramTuple]

                preceedingWord = prevTuple[0]
                prevTuple = (word, preceedingWord)

        print "Trigram estimate probability of test text: ", probability

    # predict the next word by taking a single word as input
    def predict(self, precedingTuple):
        possibilities = {}

        for gram, prob in self.trigramEst.iteritems():
            if precedingTuple == gram[1]:
                # print gram, prob
                possibilities[gram] = prob

        if len(possibilities):
            predictedValue = max(possibilities.iteritems(), key=operator.itemgetter(1))[0]
        print "Bigram predicted word for '", precedingTuple[1], "' '", precedingTuple[0], "' is: ", predictedValue[0]