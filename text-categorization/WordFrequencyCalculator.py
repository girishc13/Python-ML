'''
Document Frequency calculator for input data
'''
import collections
import re
from nltk import WordPunctTokenizer

from sentenceconstructor import SentenceConstructor


__author__ = 'girish'


class WordFrequencyCalculator(object):
    def __init__(self):
        self.sentenceConstructor = SentenceConstructor()

    def train(self, filePath):
        rawData = open(filePath, 'r').read()

        # sentenceList = re.split(r'\s', rawData)
        # # sentenceList = self.sentenceConstructor.construct(filePath, excluePunctuations=True)
        # wFCount = {}
        # for sentence in sentenceList:
        #     for token in sentence.split():
        #         if token in wFCount:
        #             wFCount[token] += 1
        #         else:
        #             wFCount[token] = 1

        wFCount = {}
        punctRegex = r'[-\.<>,\/0-9$!\'\"\(\)&*:;]'
        tokenizer = WordPunctTokenizer()
        tokenList = tokenizer.tokenize(rawData)
        for token in tokenList:
            matchPunct = re.search(punctRegex, token)
            if not matchPunct and token != '\x03':
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