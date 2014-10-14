# Naive Bayes Classifier class

# Imports
from VocabularyCalculator import VocabularyCalculator
from PriorCalculator import PriorCalculator

class NB_Classifier(): 
    
    def __init__(self, trainDir, testDir): 
        self.trainDir = trainDir
        self.testDir = testDir
        self.vocabCount = 0
        
        
    def train_classifier(self):
        vocabCalc = VocabularyCalculator()
        self.vocabCount = vocabCalc.calculate(self.trainDir)
        
        # calculate priors
        priorCalc = PriorCalculator()
        priorCalc.calculate(self.trainDir)
        print priorCalc.getPriors()
        
    