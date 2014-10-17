# Calculates the prior probabilites of the classes in the dir

# Imports
from __future__ import division
import sys
import os
import os.path

class PriorCalculator():
    
    def __init__(self):
        self.priors = {}
        
    def getPriors(self):
        return self.priors
        
    def calculate(self, dir):
        # print "Calculating priors..."
        numDocsInClass = {}
        totalNumFiles = 0
        for classDir in os.listdir(dir):            
            numDocs = len(os.listdir(os.path.join(dir, classDir)))
            numDocs -= 1
            totalNumFiles += numDocs
            numDocsInClass[classDir] = numDocs
        
        # calculate the prior by dividing the number of files in each class by
        # total number of files
        for className, numDocs in numDocsInClass.iteritems():
            self.priors[className] = numDocs / totalNumFiles
        