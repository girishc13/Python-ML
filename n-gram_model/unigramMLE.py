__author__ = 'girish'
# Unigram model MLE probability calculator

import re

class UnigramMLE():

    def __init__(self, textFileName):
        self.textFileName = textFileName
        self.unigramEst = {}
        self.unigramCount = {}

    # calculates the unigram model training parameters
    def calculateForAllDirectories(self):
        textFile = open(self.textFileName, "r")
        data = textFile.read()
        sentences = re.split(r'( *[\.])', data)
        totalWordCount = 0.0
        prevWord = "<s>"

        # Calculate total word count and number of occurrences for each word
        for sentence in sentences:
            for word in sentence.split():
                totalWordCount += 1

                if word == ".":
                    word = "<s>"

                if word in self.unigramCount:
                    self.unigramCount[word] += 1
                else:
                    self.unigramCount[word] = 1

        # calculateForAllDirectories the actual MLE estimate by dividing the word count by total no. of words
        for word, count in self.unigramCount.iteritems():
            self.unigramEst[word] = count / totalWordCount

        # print self.unigramEst
        # print self.unigramCount

    # Returns the unigram estimate dict
    def getUnigramEst(self):
        return self.unigramEst

    # Returns the unigram count of words
    def getUnigramCount(self):
        return self.unigramCount
