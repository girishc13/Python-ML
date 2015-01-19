'''
Implementation of Linear Classifier
'''
import os
import re
import operator

from FeatureCalculator import FeatureCalculator


__author__ = 'girish'


class Linear_Classifier(object):
    def __init__(self, trainDir, testDir):
        self.trainDir = trainDir
        self.testDir = testDir

    def extractSentencesFromFile(self, currentTestDir, fileName):
        textFile = open(os.path.join(self.testDir, currentTestDir, fileName), 'r')
        rawData = textFile.read()
        sentences = re.split(r'( *[\.])', rawData)
        return sentences

    def test_classifier(self):
        testDirEstimations = {}
        testDirClassEstimation = {}
        featCalculator = FeatureCalculator()
        for currentTestDir in os.listdir(self.testDir):
            fileEstimation = {}
            testDirEstimations[currentTestDir] = fileEstimation
            fileClassEstimation = {}
            testDirClassEstimation[currentTestDir] = fileClassEstimation
            for fileName in os.listdir(os.path.join(self.testDir, currentTestDir)):
                sentences = self.extractSentencesFromFile(currentTestDir, fileName)
                featClassEstimations = {}
                fileEstimation[fileName] = featClassEstimations
                for featClass in os.listdir(self.trainDir):
                    featClassEstimations[featClass] = featCalculator.estimate(sentences, featClass)
                fileClassEstimation[fileName] = max(featClassEstimations.iteritems(), key=operator.itemgetter(1))[0]
            # break

        return testDirEstimations