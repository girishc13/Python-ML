'''
Document Frequency calculator for input data
'''
import collections
import re
from sklearn import svm

from nltk import WordPunctTokenizer

from sentenceconstructor import SentenceConstructor


__author__ = 'girish'


class WordFrequencyCalculator(object):
    def __init__(self):
        self.sentenceConstructor = SentenceConstructor()

    def calculateWordFreqs(self, filePath):
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
        punctRegex = r'[-\.<>,\/0-9$!\'\"\(\)&*:;^\[\]]'
        tokenizer = WordPunctTokenizer()
        tokenList = tokenizer.tokenize(rawData)
        for token in tokenList:
            matchPunct = re.search(punctRegex, token)
            if not matchPunct and token != '\x03':
                if token.lower() in wFCount:
                    wFCount[token.lower()] += 1
                else:
                    wFCount[token.lower()] = 1

        self.__featureDict = dict((key, value) for key, value in wFCount.iteritems() if wFCount[key] >= 1)

    @property
    def featureDict(self):
        return self.__featureDict

    def calculateWfCountForInputSet(self, inputWordSet):
        self.wfCountAgg = {}
        for token in inputWordSet:
            if token in self.__featureDict:
                self.wfCountAgg[token] = self.__featureDict[token]
            else:
                self.wfCountAgg[token] = 0

        self.wfCountAgg = collections.OrderedDict(sorted(self.wfCountAgg.items()))
        return self.wfCountAgg

    def trainBinarySVM(self, negativeClassFeatureList):
        train_data = []
        train_target = []

        train_data.append(self.__featureDict.values())
        train_target.append(1)

        for negFeatures in negativeClassFeatureList:
            train_data.append(negFeatures)
            train_target.append(0)

        self.__svc = svm.SVC()
        self.__svc.fit(train_data, train_target)

        # test_predict = self.__svc.predict(self.__featureDict.values())
        test_predict = self.__svc.predict(train_data[2])

        return

    def predict(self, testFeatures):
        return self.__svc.predict(testFeatures)
