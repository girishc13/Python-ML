'''
Sentiment Analysis Classifier for training and testing IMDB data
'''
from WordFrequencyCalculatorDict import WordFrequencyCalculatorDict

__author__ = 'girish'

class SentimentAnalysisClassifier(object):
    def __init__(self):
        self.unigramCalculatorDict = WordFrequencyCalculatorDict()

    def train(self):
        # self.unigramCalculatorDict.trainNaiveBayes()
        self.unigramCalculatorDict.trainWithSVM()

    def test(self):
    #     self.unigramCalculatorDict.testWithNaiveBayes()
        self.unigramCalculatorDict.testWithSVM()

