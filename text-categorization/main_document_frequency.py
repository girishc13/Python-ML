'''
Main file for classifying reuters data using document frequency as features
'''
from WordFrequencyClassifier import WordFrequencyClassifier

__author__ = 'girish'


if __name__ == "__main__":
    classifier = WordFrequencyClassifier()
    classifier.train()
    classifier.test()