'''
Sentiment Analysis Classifier for training and testing IMDB data
'''
from UnigramCalculatorDict import UnigramCalculatorDict

__author__ = 'girish'

class SentimentAnalysisClassifier(object):
    def __init__(self):
        self.unigramCalculatorDict = UnigramCalculatorDict()

    def train(self):
        # self.unigramCalculatorDict.trainNaiveBayes()
        self.unigramCalculatorDict.trainWithSVM()

    def test(self):
    #     self.unigramCalculatorDict.testWithNaiveBayes()
        self.unigramCalculatorDict.testWithSVM()

