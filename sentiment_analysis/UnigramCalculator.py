'''
Class which performs sentiment analysis calculations on the input file
'''
from math import log
from sklearn import svm
import collections

__author__ = 'girish'


class UnigramCalculator(object):
    def calculateUnigramWordCount(self, fileName):
        textData = self.extractDataFromFile(fileName)
        self.unigramCount = {}
        for word in textData:
            if word in self.unigramCount:
                self.unigramCount[word] += 1
            else:
                self.unigramCount[word] = 1

        self.__featureDict = dict((key, value) for key, value in self.unigramCount.items() if value > 1)
        self.totalNumWords += len(self.__featureDict)


    def extractDataFromFile(self, filePath):
        textData = open(filePath, 'r').read()
        lines = textData.split()
        return lines

    def train(self, fileName):
        self.__featureDict = {}
        self.totalNumWords = 0.0
        self.calculateUnigramWordCount(fileName)
        self.vocabularyCount = len(self.__featureDict)

    def calculateWordCountForTest(self, word):
        wordCount = 0.0
        if word in self.__featureDict:
            wordCount = self.__featureDict[word]
        else:
            wordCount = 1
        return wordCount

    def calculateProbabilityForData(self, textData):
        probEst = 0.0
        for word in textData:
            wordCount = self.calculateWordCountForTest(word)
            probEst += log(wordCount / (self.totalNumWords + self.vocabularyCount))
        return probEst

    def test(self, filePath):
        textData = self.extractDataFromFile(filePath)
        probEst = self.calculateProbabilityForData(textData)
        return probEst

    def calculateFeatureList(self, filePath):
        self.train(filePath)

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

    def testWithSvm(self, testFeatures):
        return self.__svc.predict(testFeatures)
