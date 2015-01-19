'''
main file for a linear classifier
'''
import os
from LinearClassifier import Linear_Classifier

__author__ = 'girish'

if __name__ == '__main__':
    currentDir = os.curdir
    trainDir = os.path.join(currentDir, "../train")
    testDir = os.path.join(currentDir, "../test")
    classifier = Linear_Classifier(trainDir, trainDir)
    classifier.test_classifier()