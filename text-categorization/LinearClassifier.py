'''
Implementation of Linear Classifier
'''
import os
from FeatureCalculator import FeatureCalculator

__author__ = 'girish'

class Linear_Classifier(object):
    def __init__(self, trainDir, testDir):
        self.trainDir = trainDir
        self.testDir = testDir

    def createNewCalculator(self, classDir):
        calculator = FeatureCalculator()
        self.calculators[classDir] = calculator
        return calculator

    def train_classifier(self):
        self.calculators = {}
        for classDirName in os.listdir(self.trainDir):
            calculator = self.createNewCalculator(classDirName)
            calculator.train(classDirName)
