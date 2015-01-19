'''
Document Frequency calculator for input data
'''
import collections

from sentenceconstructor import SentenceConstructor


__author__ = 'girish'


class WordFrequencyCalculator(object):
    def __init__(self):
        self.sentenceConstructor = SentenceConstructor()

    def train(self, filePath):
        # rawData = open(filePath, 'r').read()
        # sentenceList = re.split(r'( *[\.])', rawData)
        sentenceList = self.sentenceConstructor.construct(filePath, excluePunctuations=True)
        wFCount = {}
        for sentence in sentenceList:
            for token in sentence:
                if token in wFCount:
                    wFCount[token] += 1
                else:
                    wFCount[token] = 1

        self.dfCountThresh = dict((key, value) for key, value in wFCount.iteritems() if wFCount[key] >= 1)

    def updateWfCount(self, aggregatedWordSet):
        self.wfCountAgg = {}
        for token in aggregatedWordSet:
            if token in self.dfCountThresh:
                self.wfCountAgg[token] = self.dfCountThresh[token]
            else:
                self.wfCountAgg[token] = 0

        self.wfCountAgg = collections.OrderedDict(sorted(self.wfCountAgg.items()))
        return self.wfCountAgg