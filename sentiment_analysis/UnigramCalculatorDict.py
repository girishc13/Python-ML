'''
Class to hold sentiment analysis unigram calculators
'''
import operator
from UnigramCalculator import UnigramCalculator

__author__ = 'girish'

class UnigramCalculatorDict(object):
    def initAndTrainClassifier(self, className, fileName):
        posCalculator = UnigramCalculator()
        self.calculators[className] = posCalculator
        posCalculator.train(fileName)

    def train(self):
        self.calculators = {}
        self.initAndTrainClassifier("pos", "mega_train_pos_doc.txt")
        self.initAndTrainClassifier("neg", "mega_train_neg_doc.txt")

    def testForFileName(self, testFileName):
        estimations = {}
        for className, calculator in self.calculators.iteritems():
            estimations[className] = calculator.test(testFileName)
        predictedClass = max(estimations.iteritems(), key=operator.itemgetter(1))[0]
        print "Predicted class for ", testFileName, "is: ", predictedClass

    def test(self):
        self.testForFileName("mega_test_pos_doc.txt")
        self.testForFileName("mega_test_neg_doc.txt")
