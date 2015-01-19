'''
Document Frequency calculator for input data
'''
import collections

from sentenceconstructor import SentenceConstructor


__author__ = 'girish'


class DocumentFrequencyCalculator(object):
    def __init__(self):
        self.sentenceConstructor = SentenceConstructor()

    def train(self, filePath):
        # rawData = open(filePath, 'r').read()
        # sentenceList = re.split(r'( *[\.])', rawData)
        sentenceList = self.sentenceConstructor.construct(filePath, excluePunctuations=True)
        dFCount = {}
        for sentence in sentenceList:
            for token in sentence:
                if token in dFCount:
                    dFCount[token] += 1
                else:
                    dFCount[token] = 1

        self.dfCountThresh = dict((key, value) for key, value in dFCount.iteritems() if dFCount[key] > 2)

    def updateDfCount(self, aggregatedWordSet):
        self.dfCountAgg = {}
        for token in aggregatedWordSet:
            if token in self.dfCountThresh:
                self.dfCountAgg[token] = self.dfCountThresh[token]
            else:
                self.dfCountAgg[token] = 0

        self.dfCountAgg = collections.OrderedDict(sorted(self.dfCountAgg.items()))
        return self.dfCountAgg