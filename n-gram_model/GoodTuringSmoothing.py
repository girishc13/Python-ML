import SentenceConstructor.sentence_constructor

__author__ = 'girish'
# Good-Turing Smoothing Calculations with sentence construction

# Imports
import re
import SentenceConstructor.sentence_constructor
import UnigramCalculator.UnigramCalculator
import operator

def displaySentences(sentences):
    for sentence in sentences:
        print sentence
        print ""

if  __name__== "__main__":
    trainConstructor1 = SentenceConstructor()
    trainSentences1 = trainConstructor1.construct("sampleText1.txt")
    # displaySentences(sentences)
    unigramCalc1 = UnigramCalculator()
    unigramCalc1.calculateForAllDirectories(trainSentences1)


    trainConstructor2 = SentenceConstructor()
    trainSentences2 = trainConstructor2.construct("sampleText2.txt")
    # displaySentences(sentences)
    unigramCalc2 = UnigramCalculator()
    unigramCalc2.calculateForAllDirectories(trainSentences2)


    testConstructor = SentenceConstructor()
    testSentences = testConstructor.construct("testText.txt")
    probEst1 = unigramCalc1.predict(testSentences)
    print probEst1
    probEst2 = unigramCalc2.predict(testSentences)
    print probEst2
    # print "Min: ", min(probEst1, probEst2)
    possibilities = [probEst1, probEst2]
    index, value = min(enumerate(possibilities), key=operator.itemgetter(1))
    print "Predicted Class: ", index + 1