from __future__ import division

__author__ = 'girish'
# Imports
from PriorCalculator import PriorCalculator
from unigramMLE import UnigramMLE
from bigramMLE import BigramMLE
from trigramMLE import TrigramMLE

# Naive Bayes Classifier using NGram Models

class NBClassifier_NGram():
    # Initialize classifier to hold the calculation parameters
    def __init__(self, trainDir, testDir):
        self.trainDir = trainDir
        self.testDir = testDir
        self.priors = {}
        self.unigramCount = {}
        self.unigramProb = {}
        self.bigramCount = {}
        self.bigramProb = {}
        self.trigramCount = {}
        self.trigramProb = {}

        self.unigramCalc = UnigramMLE(self.trainDir)
        self.bigramCalc = BigramMLE(self.trainDir)
        self.trigramCalc = TrigramMLE(self.trainDir)

    # train the classifier using n-gram models to obtain the counts and probabilities
    def train_classifier(self):

        # calculate the prior probabilities of the classes
        priorCalc = PriorCalculator()
        priorCalc.calculate(self.trainDir)
        self.priors = priorCalc.getPriors()
        print "Posterior Probs: ", self.priors


        # perform unigram model calculations
        print "Calculating Unigram model parameters..."
        self.unigramCalc.calculate()

        self.unigramCount = self.unigramCalc.getUnigramCount()
        self.unigramProb = self.unigramCalc.getUnigramProb()

        # perform bigram model calculations
        print "Calculating Bigram model parameters..."
        self.bigramCalc.calculate(self.unigramCount)

        self.bigramCount = self.bigramCalc.getBigramCount()
        self.bigramProb = self.bigramCalc.getBigramProb()

        # perform trigram model calculations
        print "Calculating Trigram model parameters..."
        self.trigramCalc.calculate(self.bigramCount)

        self.trigramCount = self.trigramCalc.getTrigramCount()
        self.trigramProb = self.trigramCalc.getTrigramProb()



    # test the classifier using n-gram models
    def test_classifier(self):

        # calculate conditional probabilities of the test class using bigram model
        self.bigramCalc.estimateProbability(self.testDir, self.priors, self.unigramProb)


        print ""
        # calculate conditional probabilities of the test class using trigram model
        self.trigramCalc.estimateProbability(self.testDir, self.priors, self.unigramProb, self.bigramProb)