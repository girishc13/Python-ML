'''
Created on Dec 22, 2014
Main file for n-gram text classification using good-turing smoothing
@author: girish
'''
# Imports
import os.path

from SimpleClassifier import SimpleClassifier


def buildTrainDirectory():
    currentDir = os.curdir
    trainDir = os.path.abspath(os.path.join(currentDir, os.pardir, os.pardir, "train"))
    return trainDir


def buildTestDirectory():
    currentDir = os.curdir
    testDir = os.path.abspath(os.path.join(currentDir, os.pardir, os.pardir, "test"))
    return testDir


def createClassifier():
    trainDir = buildTrainDirectory()
    classifier = SimpleClassifier(trainDir)
    return classifier


if __name__ == "__main__":
    classifier = createClassifier()
    classifier.train_classifier()
    classifier.test_classifier(buildTestDirectory())
    print "Done."
