# Posterior Probability calculator

# Imports
from __future__ import division
import sys
import os
import os.path
from VocabularyCalculator import VocabularyCalculator

class PosteriorProbCalc():

    def calcPosteriorProb(self, dir, priors, condProb):

         cmap = {}

         # vocabCalc = VocabularyCalculator()
         # vocabCalc.calculate(dir)
         #
         # print "Test class vocab count: ", vocabCalc.getClassVocabCount()

         for classDir in os.listdir(dir):
             classVocab = {}
             if classDir == 'grain':

                 filename = classDir + "_mega.txt"
                 testFile = open(os.path.join(dir, classDir, filename), "r")

                 for line in testFile:
                     words = line.split()

                     for word in words:
                         if word in classVocab:
                             classVocab[word] += 1
                         else:
                             classVocab[word] = 1


                 # calculate cmap
                 cmap[classDir] = {}
                 for trainClass, classPrior in priors.iteritems():
                     prod = classPrior

                     for word, count in classVocab.iteritems():
                        print word, count
                        prod = prod * condProb[trainClass][word]

                     cmap[classDir][trainClass] = prod

         return cmap
