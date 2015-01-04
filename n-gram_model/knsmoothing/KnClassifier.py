'''
Simple classifier for Kneser-Ney smoothing
'''
from gtsmoothing.EstimatorAndLookUp import EstimatorAndLookUp
from UnigramCalculatorDict import UnigramCalculatorDict
from BigramCalculatorDict import BigramCalculatorDict
from PredictorAndLookUp import PredictorAndLookUp

__author__ = 'girish'

class KnClassifier():
    def __init__(self, trainDir):
        self.trainDir = trainDir
        self.unigramCalcDict = UnigramCalculatorDict(self.trainDir)
        self.bigramCalcDict = BigramCalculatorDict(self.trainDir, self.unigramCalcDict)

    def train_classifier(self):
        print "Training classifier..."
        print "Calculating Unigram parameters..."
        self.unigramCalcDict.calculateForAllDirectories()
        print "Calculating Bigram parameters..."
        self.bigramCalcDict.calculateForAllDirectories()

    def test_classifier(self, testDir):
        pass
        # print "Testing input data set with unigram model..."
        # unigramProbEstimator = EstimatorAndLookUp()
        # unigramProbEstimator.estimate(testDir, self.unigramCalcDict)
        # unigramProbEstimator.calculateMinEstimations()
        # unigramProbEstimator.calculateAndPrintAccuracies()

        # print "Testing input data set with bigram model..."
        # bigramProbEstimator = EstimatorAndLookUp()
        # bigramProbEstimator.estimate(testDir, self.bigramCalcDict)
        # bigramProbEstimator.calculateMinEstimations()
        # bigramProbEstimator.calculateAndPrintAccuracies()

    def predict(self, word):
        predictor = PredictorAndLookUp()
        return predictor.predict(word.lower(), self.bigramCalcDict)
