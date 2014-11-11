from __future__ import division
__author__ = 'girish'
# Bigram model MLE probability calculator and estimator

import re
import operator
import os
import numpy as np
from math import log

class BigramMLE():

    def __init__(self, dirName):
        self.dirName = dirName
        self.bigramProb = {}
        self.bigramCount = {}

    # calculates the bigram model training parameters
    def calculate(self, unigramCount):

        # iterate through the directory
        for classDir in os.listdir(self.dirName):
            self.bigramProb[classDir] = {}
            self.bigramCount[classDir] = {}

            filename = classDir + "_" + "mega.txt"

            textFile = open(os.path.join(self.dirName, classDir, filename), "r")
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

                    if bigramTuple in self.bigramCount[classDir]:
                        self.bigramCount[classDir][bigramTuple] += 1
                    else:
                        self.bigramCount[classDir][bigramTuple] = 1

                    prevWord = word

            # calculate count by dividing from unigram count
            for gram, count in self.bigramCount[classDir].iteritems():
                precedingGram = gram[1]
                self.bigramProb[classDir][gram] = self.bigramCount[classDir][gram] / unigramCount[classDir][precedingGram]
                # print gram, self.bigramEst[gram], precedingGram, unigramCount[precedingGram]


            # print calculated probaility
            # for gram, count in self.bigramEst.iteritems():
            #     print gram, count

    # Returns the bigram calculations for the initialized text
    def getBigramProb(self):
        return self.bigramProb

    # Returns the bigram count for the initialized text
    def getBigramCount(self):
        return self.bigramCount

    # estimates the probability of the input text from the calculated estimates
    def estimateProbability(self, dir, priorProb):

        totalCmap = {}
        print "Estimating using Bigram model..."
        correctClassEstimation = 0
        numberOfTestClasses = 0

        for classDir in os.listdir(dir):
            # if classDir == "interest":
            if 1:
                numberOfTestClasses += 1
                currentCmap = {}
                totalCmap[classDir] = {}
                filename = classDir + "_" + "mega.txt"

                textFile = open(os.path.join(dir, classDir, filename), "r")
                data = textFile.read()
                sentences = re.split(r'( *[\.])', data)

                tempFile = open("temp_bigram.txt", "w")
                for trainClass, classPrior in priorProb.iteritems():
                    # probability = np.float128(1.0)
                    probability = np.float128(0.0)

                    prevWord = "<s>"
                    for sentence in sentences:

                        for word in sentence.split():
                            if word == ".":
                                word = "<s>"

                            bigramTuple = (word, prevWord)

                            if self.bigramProb[trainClass].has_key(bigramTuple):
                                # print bigramTuple, self.bigramEst[bigramTuple], probability
                                # probability *= self.bigramProb[trainClass][bigramTuple]

                                # calculate in terms of perplexity
                                # probability  += pow(self.bigramProb[trainClass][bigramTuple], -(1/3))

                                # calculate in terms of log
                                probability += log(self.bigramProb[trainClass][bigramTuple])

                                tempFile.write(trainClass + " " + str(bigramTuple) + " " + str(self.bigramProb[trainClass][bigramTuple]) + " "
                                                + str(probability))
                                tempFile.write("\n")


                            prevWord = word

                    # currentCmap[trainClass] = probability * np.float128(classPrior)
                    # currentCmap[trainClass] = probability
                    currentCmap[trainClass] = probability + log(classPrior)

                totalCmap[classDir] = currentCmap
                # print "Total Conditional Probability Map: "
                # print totalCmap[classDir]

                # estimatedClass = max(currentCmap.iteritems(), key=operator.itemgetter(1))[0]
                estimatedClass = min(currentCmap.iteritems(), key=operator.itemgetter(1))[0]
                if(estimatedClass == classDir):
                    correctClassEstimation += 1
                print "Estimated Class for test class", classDir, "is: ", estimatedClass

        accuracy = (correctClassEstimation / numberOfTestClasses) * 100
        print "Accuracy using Bigram model:", accuracy, "%"

        tempFile.close()


    # predict the next word by taking a bigram tuple word as input
    def predict(self, precedingWord):
        possibilities = {}

        for gram, prob in self.bigramProb.iteritems():
            if precedingWord == gram[1]:
                print gram, prob
                possibilities[gram] = prob

        predictedValue = max(possibilities.iteritems(), key=operator.itemgetter(1))[0]
        print "Bigram predicted word for ", precedingWord, " is: ", predictedValue[0]