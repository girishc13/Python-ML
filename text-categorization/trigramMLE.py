from __future__ import division
__author__ = 'girish'

# Trigram Model MLE probability calculator and estimator

import re
import operator
import os
import numpy as np

class TrigramMLE():

    def __init__(self, dirName):
        self.dirName = dirName
        self.trigramProb = {}
        self.trigramCount = {}

    # calculates the trigram model training parameters
    def calculate(self, bigramCount):

        # iterate through the directory
        for classDir in os.listdir(self.dirName):
            self.trigramProb[classDir] = {}
            self.trigramCount[classDir] = {}

            filename = classDir + "_" + "mega.txt"

            textFile = open(os.path.join(self.dirName, classDir, filename), "r")
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
                        self.trigramCount[classDir][trigramTuple] += 1
                    else:
                        self.trigramCount[classDir][trigramTuple] = 1

                    preceedingWord = prevTuple[0]
                    prevTuple = (word, preceedingWord)

            # print self.trigramCount

            # calculate probalities using the count
            for gram, count in self.trigramCount[classDir].iteritems():
                preceedingTuple = gram[1]
                if bigramCount[classDir].has_key(preceedingTuple):
                    self.trigramProb[classDir][gram] = self.trigramCount[classDir][gram] / bigramCount[classDir][preceedingTuple]

            # print calculated probability
            # for gram, prob in self.trigramEst.iteritems():
            #     print gram, prob

    # Returns the trigram calculations for initialized text
    def getTrigramProb(self):
        return self.trigramProb

    # Returns the trigram count
    def getTrigramCount(self):
        return self.trigramCount

    # estimates the probability of the input text from the calculated estimates
    def estimateProbability(self, dir, priorProb):

        totalCmap = {}
        print "Estimating using Trigram model..."
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

                tempFile = open("temp_trigram.txt", "w")
                for trainClass, classPrior in priorProb.iteritems():
                    probability = np.float128(1.0)

                    prevTuple = ("<s>", "<s>")
                    for sentence in sentences:

                        for word in sentence.split():
                            if word == ".":
                                word = "<s>"

                            trigramTuple = (word, prevTuple)

                            if self.trigramProb[trainClass].has_key(trigramTuple):
                                # probability *= self.trigramProb[trigramTuple]

                                # calculate in terms of perplexity
                                probability += pow(self.trigramProb[trainClass][trigramTuple], -(1/3))
                                tempFile.write(trainClass + " " + str(trigramTuple) + " " + str(self.trigramProb[trainClass][trigramTuple]) + " "
                                                + str(probability))
                                tempFile.write("\n")

                            preceedingWord = prevTuple[0]
                            prevTuple = (word, preceedingWord)

                    # currentCmap[trainClass] = probability * np.float128(classPrior)
                    currentCmap[trainClass] = probability

                totalCmap[classDir] = currentCmap
                # print "Total Conditional Probability Map: "
                # print totalCmap[classDir]

                estimatedClass = max(currentCmap.iteritems(), key=operator.itemgetter(1))[0]
                if(estimatedClass == classDir):
                    correctClassEstimation += 1
                print "Estimated Class for test class", classDir, "is: ", estimatedClass
                # print "Trigram estimate probability of test text: ", probability

        accuracy = (correctClassEstimation / numberOfTestClasses) * 100
        print "Accuracy using Trigram model: ", accuracy, "%"

        tempFile.close()

    # predict the next word by taking a single word as input
    def predict(self, precedingTuple):
        possibilities = {}

        print "Possibilities: "
        for gram, prob in self.trigramProb.iteritems():
            if precedingTuple == gram[1]:
                # print gram, prob
                print (precedingTuple[1], precedingTuple[0]), ": " , gram[0], " with probability: ", prob, " perplexity: ", pow(prob, -(1/3))
                possibilities[gram] = prob

        if len(possibilities):
            predictedValue = max(possibilities.iteritems(), key=operator.itemgetter(1))[0]
            print "Trigram predicted word for '", precedingTuple[1], "' '", precedingTuple[0], "' is: ", predictedValue[0]
        else:
            print "Input word sequence was not seen before."
