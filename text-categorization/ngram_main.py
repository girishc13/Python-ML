__author__ = 'girish'
# Main file for Naive Bayes Classifier using N-Gram models

# Imports
import sys
import os
import os.path
from NBClassifier_NGram import NBClassifier_NGram

if __name__ == "__main__":
    currentDir = os.curdir
    trainDir = os.path.join(currentDir, "train")
    testDir = os.path.join(currentDir, "test")
    classifier = NBClassifier_NGram(trainDir, testDir)
    classifier.train_classifier()

    classifier.test_classifier()
