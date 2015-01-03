"""
Class which holds the unigram probability estimations of a test directory 
against all the train class
"""
from SentenceConstructor import SentenceConstructor

class Estimator():
    

    def constructSentences(self, filePath):
        sentConstructor = SentenceConstructor()
        sentences = sentConstructor.construct(filePath)
        return sentences

    def estimate(self, filePath, trainClassifiers):
        sentences = self.constructSentences(filePath)
        self.estimates = {}
        for trainClass, classifier in trainClassifiers.items():
            self.estimates[trainClass] = classifier.estimateProbability(sentences)
    
        return self.estimates