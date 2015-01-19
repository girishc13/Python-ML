'''
Main file for classifying reuters data using document frequency as features
'''
from DocumentFrequencyClassifier import DocumentFrequencyClassifier

__author__ = 'girish'


if __name__ == "__main__":
    classifier = DocumentFrequencyClassifier()
    classifier.train()
    classifier.test()