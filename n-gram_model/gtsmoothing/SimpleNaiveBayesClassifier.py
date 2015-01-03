from UnigramCalculatorDict import UnigramCalculatorDict

__author__ = 'girish'

class SimpleNaiveBayesClassifier():
    def __init__(self, traindir):
        self.trainDir = traindir
        self.unigramCalculators = UnigramCalculatorDict(traindir)

    def train_classifier(self):
        print "Training Classifier..."
        self.unigramCalculators.calculateForAllDirectories()

        print "Finished training."