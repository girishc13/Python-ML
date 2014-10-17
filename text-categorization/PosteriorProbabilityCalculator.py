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

         for classDir in os.listdir(dir):
             classVocab = {}
             currentCmap = {}
             # if classDir == 'earn':

             filename = classDir + "_mega.txt"
             testFile = open(os.path.join(dir, classDir, filename), "r")

             for line in testFile:
                 words = line.split()

                 for word in words:
                     if word in classVocab:
                         classVocab[word] += 1
                     else:
                         classVocab[word] = 1


             # calculate currentCmap
             totalCmap[classDir] = {}
             tempFile = open("temp.txt", "w")
             for trainClass, classPrior in priors.iteritems():
                 prod = np.float128(1.0)

                 for word, count in classVocab.iteritems():
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

             # print "Actual Test class: ", classDir, ", Estimated Test class: " , max(currentCmap.iteritems(), key=operator.itemgetter(1))[0]
                 totalCmap[classDir] = currentCmap
             # print "Current cmap: ", currentCmap
             # print "max: ", max(currentCmap.values())
             # print "\n"

             print "Actual Test class: ", classDir, ", Estimated Test class: " , max(currentCmap.iteritems(),
             key=operator.itemgetter(1))[0]
             # print "\n"

         return totalCmap
