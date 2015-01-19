from sentenceconstructor import SentenceConstructor

__author__ = 'girish'
# Good-Turing Smoothing Calculations with sentence construction

# Imports
import re
from sentenceconstructor import  SentenceConstructor
from UnigramCalculator import UnigramCalculator

def displaySentences(sentences):
    for sentence in sentences:
        print sentence
        print ""

if  __name__== "__main__":
    trainConstructor1 = SentenceConstructor()
    trainSentences1 = trainConstructor1.construct("sample_text1.txt")
    # displaySentences(sentences)
    unigramCalc1 = UnigramCalculator()
    unigramCalc1.calculate(trainSentences1)


    trainConstructor2 = SentenceConstructor()
    trainSentences2 = trainConstructor2.construct("sample_text2.txt")
    # displaySentences(sentences)
    unigramCalc2 = UnigramCalculator()
    unigramCalc2.calculate(trainSentences2)


    testConstructor = SentenceConstructor()
    testSentences = testConstructor.construct("test_text.txt")
    probEst1 = unigramCalc1.predict(testSentences)
    print probEst1
    probEst2 = unigramCalc2.predict(testSentences)
    print probEst2
    print "Max: ", max(probEst1, probEst2)