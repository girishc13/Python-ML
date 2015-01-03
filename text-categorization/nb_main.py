# Naive Bayes Classifier Main

# Imports
import sys
import os
import os.path
from NB_Classifier import NB_Classifier

if __name__ == "__main__":
    currentDir = os.curdir
    trainDir = os.path.join(currentDir, "../train")
    testDir = os.path.join(currentDir, "../test")
    classifier = NB_Classifier(trainDir, testDir)
    classifier.train_classifier()

    classifier.test_classifier()

