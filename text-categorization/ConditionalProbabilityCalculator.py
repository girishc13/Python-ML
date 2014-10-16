# Conditional Probability Calculator

# Imports
from __future__ import division
import sys
import os
import os.path

class ConditionalProbCalc():

    def  __init__(self):
        self.condProb = {}

    def calculateConditionalProb(self, dir, classVocabCount, vocabCount):

        for classDir in os.listdir(dir):
            self.condProb[classDir] = {}
            file = None
            filename = classDir + "_" + "mega.txt"

            file = open(os.path.join(dir, classDir, filename), "r")
            # count the number of times each word occurs in a class
            for line in file:
                words = line.split()
                for word in words:
                    if word in self.condProb[classDir]:
                        self.condProb[classDir][word] += 1
                    else:
                        self.condProb[classDir][word] = 1

            file.close()

            # for each word in each class calculate the conditional probability
            denom = classVocabCount[classDir] + vocabCount
            for word in self.condProb[classDir]:
                self.condProb[classDir][word] = (self.condProb[classDir][word] + 1) / denom


            print "Number of unique words in ", classDir, " is ", len(self.condProb[classDir])

        # print "Conditional Prob of words in class 'grain': "
        # for word in self.condProb['grain']:
        #     print word, ": ", self.condProb['grain'][word]

    def getCondProb(self):
        return self.condProb