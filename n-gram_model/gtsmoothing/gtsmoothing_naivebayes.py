import os

__author__ = 'girish'
"""
Main file for Text classification using Naive Bayes
classifier and Good-Turing smoothing
"""

from SimpleNaiveBayesClassifier import SimpleNaiveBayesClassifier


def buildTrainDirectory():
    currentDir = os.curdir
    trainDir = os.path.abspath(os.path.join(currentDir, os.pardir, os.pardir, "train"))
    return trainDir


def createClassifier():
    classifier = SimpleNaiveBayesClassifier(buildTrainDirectory())
    return classifier


if __name__ == "__main__":
    classifier = createClassifier()
    classifier.train_classifier()