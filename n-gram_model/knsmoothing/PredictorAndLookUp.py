'''
Predictor class predicts the next word for the input word
'''
__author__ = 'girish'

class PredictorAndLookUp(object):

    def predict(self, word, bigramCalcDict):
        possibleWordProbs = {}
        for trainClass, classifier in bigramCalcDict.getCalculators().items():
            possibleWordProbs[trainClass] = classifier.predict(word)

        print possibleWordProbs
