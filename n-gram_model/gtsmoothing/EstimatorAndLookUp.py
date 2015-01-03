"""
Class which holds the dictionary of probability estimations of each test 
directory
"""

import operator
import os

from Estimator import Estimator


class EstimatorAndLookUp():
    def createEstimator(self, classDir, fileName):
        estimator = Estimator()
        self.estimations[classDir][fileName] = estimator
        return estimator

    def createFilePath(self, testDir, classDir, fileName):
        # fileName = "std_text.txt"
        # fileName = classDir + "_" + "mega.txt"
        filePath = os.path.abspath(os.path.join(testDir, classDir, fileName))
        return filePath

    def estimate(self, testDir, trainClassifiers):
        self.estimations = {}
        for classDir in os.listdir(testDir):
            absClassPath = os.path.abspath(os.path.join(testDir, classDir))
            self.estimations[classDir] = {}
            for fileName in os.listdir(absClassPath):
                estimator = self.createEstimator(classDir, fileName)
                filePath = self.createFilePath(testDir, classDir, fileName)
                self.estimations[classDir][fileName] = estimator.estimate(filePath, trainClassifiers.getCalculators())

    def calculateMinEstimations(self):
        self.minEstimations = {}
        for testClass, classEstimations in self.estimations.items():
            self.minEstimations[testClass] = {}
            for fileName, estimations in classEstimations.items():
                minClass = min(estimations.iteritems(), key=operator.itemgetter(1))[0]
                self.minEstimations[testClass][fileName] = minClass

    def printMinEstimations(self):
        for testClass, minEstClass in self.minEstimations.items():
            print "Test class: ", testClass
            for fileName, minEst in minEstClass.items():
                print "File Name: ", fileName, ", Estimated Class: ", minEst

    def calculateAndPrintAccuracies(self):
        self.accuracies = {}
        for testClass, minEstClass in self.minEstimations.items():
            accuracy = 0.0
            for fileName, minEst in minEstClass.items():
                if minEst == testClass:
                    accuracy += 1
            self.accuracies[testClass] = accuracy * 100 / len(minEstClass)
            print "Test Class: ", testClass, ", Accuracy: ", self.accuracies[testClass], "%"
