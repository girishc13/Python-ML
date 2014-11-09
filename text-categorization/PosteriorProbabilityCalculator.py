# Posterior Probability calculator

# Imports
from __future__ import division
import sys
import os
import os.path
import numpy as np
import operator
from VocabularyCalculator import VocabularyCalculator

class PosteriorProbCalc():

    def calcPosteriorProb(self, dir, priors, condProb):

        totalCmap = {}
        # vocabCalc = VocabularyCalculator()
        # vocabCalc.calculate(dir)
        #
        # print "Test class vocab count: ", vocabCalc.getClassVocabCount()
        testDir = "earn"
        correctClassEstimation = 0
        numberOfTestClass = 0

        for classDir in os.listdir(dir):
            # if classDir == testDir:
            if 1:
                numberOfTestClass += 1

                filename = classDir + "_" + "mega.txt"

                docVocab = {}
                currentCmap = {}
                testFile = open(os.path.join(dir, classDir, filename), "r")

                for line in testFile:
                    words = line.split()

                    for word in words:
                        if word in docVocab:
                            docVocab[word] += 1
                        else:
                            docVocab[word] = 1


                # calculate currentCmap
                totalCmap[filename] = {}
                tempFile = open("temp.txt", "w")
                for trainClass, classPrior in priors.iteritems():
                    prod = np.float128(1.0)

                    for word, count in docVocab.iteritems():
                        # print word, count
                        if word in condProb[trainClass]:
                            prod = prod * condProb[trainClass][word]
                            # print prod
                            # if condProb[trainClass][word] == 0.0:
                            # print trainClass, word, condProb[trainClass][word]
                            tempFile.write(trainClass + " " + word + " " + str(condProb[trainClass][word]) + " "
                                           + str(prod))
                            tempFile.write("\n")


                    currentCmap[trainClass] = prod * np.float128(classPrior)

                totalCmap[filename] = currentCmap
                estimatedClass = max(currentCmap.iteritems(), key=operator.itemgetter(1))[0]
                print "Actual file class: ", classDir, ", Estimated file class: " , estimatedClass
                # print "\n"
                if(estimatedClass == classDir):
                    correctClassEstimation += 1

        accuracy = (correctClassEstimation / numberOfTestClass) * 100
        print "Accuracy :", accuracy, "%"


        tempFile.close()
        return totalCmap
