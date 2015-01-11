'''
Main file for testing sentiment analysis on IMDB data
'''
from SentimentAnalysisClassifier import SentimentAnalysisClassifier

__author__ = 'girish'

if __name__ == "__main__":
    classifier = SentimentAnalysisClassifier()
    classifier.train()
    classifier.test()