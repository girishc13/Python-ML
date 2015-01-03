'''
Simple Classifier class for good-turing smoothing text classification

'''

from UnigramCalculatorDict import UnigramCalculatorDict
from EstimatorAndLookUp import EstimatorAndLookUp
from BigramCalculatorDict import BigramCalculatorDict
from TrigramCalculatorDict import TrigramCalculatorDict


class SimpleClassifier():
         
    def __init__(self, trainDir):
        self.trainDir = trainDir
        self.unigramCalcDict = UnigramCalculatorDict(self.trainDir)
        self.bigramCalcDict = BigramCalculatorDict(self.trainDir)
        self.trigramCalcDict = TrigramCalculatorDict(self.trainDir)

    
    def train_classifier(self):
        print "Training classifier..."
        print "Calculating Unigram parameters..."
        self.unigramCalcDict.calculateForAllDirectories()
        print "Calculating Bigram parameters..."
        self.bigramCalcDict.calculateForAllDirectories()
        print "Calculating Trigram paramters..."
        self.trigramCalcDict.calculateForAllDirectories()

    def test_classifier(self, testDir):
        print "Testing input data set with unigram model..."
        unigramProbEstimator = EstimatorAndLookUp()
        unigramProbEstimator.estimate(testDir, self.unigramCalcDict)
        unigramProbEstimator.calculateMinEstimations()
        # unigramProbEstimator.printMinEstimations()
        unigramProbEstimator.calculateAndPrintAccuracies()

        print "Testing input data set with bigram model..."
        bigramProbEstimator = EstimatorAndLookUp()
        bigramProbEstimator.estimate(testDir, self.bigramCalcDict)
        bigramProbEstimator.calculateMinEstimations()
        # bigramProbEstimator.printMinEstimations()
        bigramProbEstimator.calculateAndPrintAccuracies()

        print "Testing input data set with trigaram model..."
        trigramProbEstimator = EstimatorAndLookUp()
        trigramProbEstimator.estimate(testDir, self.trigramCalcDict)
        trigramProbEstimator.calculateMinEstimations()
        trigramProbEstimator.calculateAndPrintAccuracies()