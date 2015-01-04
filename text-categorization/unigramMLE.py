from math import log
import operator

__author__ = 'girish'
# Unigram model MLE probability calculator

# Imports
import re
import os


class UnigramMLE():
    def __init__(self, dirName):
        self.dirName = dirName
        self.unigramProb = {}
        self.unigramCount = {}

    # calculates the unigram model training parameters
    def calculate(self):

        # iterate through the directory
        for classDir in os.listdir(self.dirName):
            self.unigramProb[classDir] = {}
            self.unigramCount[classDir] = {}

            filename = classDir + "_" + "mega.txt"

            textFile = open(os.path.join(self.dirName, classDir, filename), "r")
            data = textFile.read()
            sentences = re.split(r'( *[\.])', data)
            totalWordCount = 0.0
            # prevWord = "<s>"

            # Calculate total word count and number of occurrences for each word
            for sentence in sentences:
                for word in sentence.split():
                    totalWordCount += 1

                    # if word == ".":
                    # word = "<s>"

                    if word in self.unigramCount[classDir]:
                        self.unigramCount[classDir][word] += 1
                    else:
                        self.unigramCount[classDir][word] = 1

            # calculate the actual MLE estimate by dividing the word count by total no. of words
            for word, count in self.unigramCount[classDir].iteritems():
                self.unigramProb[classDir][word] = count / totalWordCount

                # print self.unigramEst
                # print self.unigramCount

    # Returns the unigram estimate dict
    def getUnigramProb(self):
        return self.unigramProb

    # Returns the unigram count of words
    def getUnigramCount(self):
        return self.unigramCount

    def estimateProbabilities(self, testDir, priorProbs):
        self.allTestClassEstimations = {}

        for classDir in os.listdir(testDir):
            testClassEstimations = {}
            self.allTestClassEstimations[classDir] = testClassEstimations

            # filename = classDir + "_" + "mega.txt"

            for filename in os.listdir(os.path.join(testDir, classDir)):
                fileEstimations = {}
                testClassEstimations[filename] = fileEstimations
                textFile = open(os.path.join(testDir, classDir, filename), "r")
                data = textFile.read()
                sentences = re.split(r'( *[\.])', data)

                tempFile = open("temp_bigram.txt", "w")
                for trainClass, classPrior in priorProbs.iteritems():

                    probEst = log(classPrior)
                    for sentence in sentences:
                        for word in sentence.split():
                            if word in self.unigramProb[trainClass]:
                                probEst += log(self.unigramProb[trainClass][word])

                    fileEstimations[trainClass] = probEst

    def calculateAndPrintAccuracies(self):
        self.accuracies = {}

        for testClass, classEstimations in self.allTestClassEstimations.items():
            accuracy = 0.0
            for filename, fileEstimations in classEstimations.iteritems():
                estimatedClass = min(fileEstimations.iteritems(), key=operator.itemgetter(1))[0]
                if estimatedClass == testClass:
                    accuracy += 1

            accuracyPer = accuracy * 100 / len(classEstimations)
            self.accuracies[testClass] = accuracyPer
            print "Test Class: ", testClass, ", Accuracy: ", accuracyPer, "%"