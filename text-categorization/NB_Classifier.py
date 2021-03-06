# Naive Bayes Classifier class

# Imports
from VocabularyCalculator import VocabularyCalculator
from PriorCalculator import PriorCalculator
from ConditionalProbabilityCalculator import ConditionalProbCalc
from PosteriorProbabilityCalculator import PosteriorProbCalc

class NB_Classifier(): 
    
    def __init__(self, trainDir, testDir): 
        self.trainDir = trainDir
        self.testDir = testDir
        self.vocabCount = 0
        self.classVocabCount = {}
        self.priors = {}
        self.condProb = {}
        
        
    def train_classifier(self):
        # calculate vocab count of all words in train set and each class
        vocabCalc = VocabularyCalculator()
        self.vocabCount = vocabCalc.calculate(self.trainDir)
        self.classVocabCount = vocabCalc.getClassVocabCount()
        print "Each class word count: " , self.classVocabCount
        
        # calculate priors
        priorCalc = PriorCalculator()
        priorCalc.calculate(self.trainDir)
        self.priors = priorCalc.getPriors()
        print "Posterior Probs: ", self.priors

        # calculate conditional probability
        condProbCalc = ConditionalProbCalc()
        condProbCalc.calculateConditionalProb(self.trainDir, self.classVocabCount, self.vocabCount)
        self.condProb = condProbCalc.getCondProb()
        
    def test_classifier(self):
        postProbCalc = PosteriorProbCalc()
        totalCmap = postProbCalc.calcPosteriorProb(self.testDir, self.priors, self.condProb)
        # print "Posterior Probs of 'earn' test class: ", totalCmap['earn']

        # print "\n"
        # for testClass, cmap in totalCmap.iteritems():
        #     print "Posterior probality of test class '", testClass ,"': ", cmap.values()
        #     print "\n"