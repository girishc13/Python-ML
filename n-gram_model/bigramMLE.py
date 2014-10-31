from __future__ import division
__author__ = 'girish'
# Bigram model MLE probability calculator and estimator

import re
import operator

class BigramMLE():

    def __init__(self, textFileName):
        self.textFileName = textFileName
        self.bigramEst = {}
        self.bigramCount = {}

    # calculates the bigram model training parameters
    def calculate(self, unigramCount):
        textFile = open(self.textFileName, "r")
        data = textFile.read()
        sentences = re.split(r'( *[\.])', data)
        # print sentences

        prevWord = "<s>"
        for sentence in sentences:
            # print sentence
            for word in sentence.split():
                if word == ".":
                    word = "<s>"

                bigramTuple = (word, prevWord)

                if bigramTuple in self.bigramCount:
                    self.bigramCount[bigramTuple] += 1
                else:
                    self.bigramCount[bigramTuple] = 1

                prevWord = word

        # calculate count by dividing from unigram count
        for gram, count in self.bigramCount.iteritems():
            precedingGram = gram[1]
            self.bigramEst[gram] = self.bigramCount[gram] / unigramCount[precedingGram]
            # print gram, self.bigramEst[gram], precedingGram, unigramCount[precedingGram]


        # print calculated probaility
        # for gram, count in self.bigramEst.iteritems():
        #     print gram, count

    # Returns the bigram calculations for the initialized text
    def getBigramEst(self):
        return self.bigramEst

    # Returns the bigram count for the initialized text
    def getBigramCount(self):
        return self.bigramCount

    # estimates the probability of the input text from the calculated estimates
    def estimateProbability(self, textFileName):
        textFile = open(textFileName, "r")
        data = textFile.read()
        sentences = re.split(r'( *[\.])', data)
        probability = 1.0

        prevWord = "<s>"
        for sentence in sentences:

            for word in sentence.split():
                if word == ".":
                    word = "<s>"

                bigramTuple = (word, prevWord)

                if self.bigramEst.has_key(bigramTuple):
                    # print bigramTuple, self.bigramEst[bigramTuple], probability
                    probability *= self.bigramEst[bigramTuple]

                prevWord = word

        print "Bigram estimate probability of test text: ", probability

    # predict the next word by taking a bigram tuple word as input
    def predict(self, precedingWord):
        possibilities = {}

        for gram, prob in self.bigramEst.iteritems():
            if precedingWord == gram[1]:
                print gram, prob
                possibilities[gram] = prob

        predictedValue = max(possibilities.iteritems(), key=operator.itemgetter(1))[0]
        print "Bigram predicted word for ", precedingWord, " is: ", predictedValue[0]