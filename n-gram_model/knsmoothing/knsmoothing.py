'''
Main file for text-classification using Kneser-Ney smoothing
'''
import os
import sys
from KnClassifier import KnClassifier

__author__ = 'girish'


def addGtSmoothingPackageToPath():
    global currDir, gtsmoothing_path
    currDir = os.curdir
    gtsmoothing_path = os.path.abspath(os.path.join(currDir, os.pardir, "gtsmoothing"))
    sys.path.append(gtsmoothing_path)


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
    classifier = KnClassifier(trainDir)
    return classifier


if __name__ == "__main__":
    addGtSmoothingPackageToPath()
    classifier = createClassifier()
    classifier.train_classifier()
    classifier.test_classifier(buildTestDirectory())
    print "Done."