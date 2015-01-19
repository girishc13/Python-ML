'''
Class to hold all the DF calculators for the classification task
'''
import os
from sklearn import svm

from WordFrequencyCalculator import WordFrequencyCalculator


__author__ = 'girish'


class WordFrequencyCalculatorDict(object):
    def train(self):
        self.calculators = {}
        self.aggregatedWordSet = set()
        for trainDir in os.listdir(os.path.join(os.curdir, os.pardir, 'train')):
            calculator = WordFrequencyCalculator()
            self.calculators[trainDir] = calculator
            filePath = os.path.join(os.curdir, os.pardir, 'train', trainDir, trainDir + '_mega.txt')
            calculator.train(filePath)
            self.aggregatedWordSet.update(calculator.dfCountThresh)

        for trainDir in os.listdir(os.path.join(os.curdir, os.pardir, 'train')):
            self.calculators[trainDir].updateWfCount(self.aggregatedWordSet)

        self.trainClassList = self.calculators.keys()
        self.target = [i for i in range(0, len(self.trainClassList))]
        self.data = [self.calculators[key].wfCountAgg.values() for key in  self.trainClassList]
        self.svc = svm.SVC()
        self.svc.fit(self.data, self.target)

    def test(self):
        testDirEstimations = {}
        testDirPredictions = {}
        testDirAccuracy = {}
        for testDir in os.listdir(os.path.join(os.curdir, os.pardir, 'test')):
            fileEstimations = {}
            testDirEstimations[testDir] = fileEstimations
            filePredictions = {}
            testDirPredictions[testDir] = filePredictions
            correctPrediction = 0.0
            for fileName in os.listdir(os.path.join(os.curdir, os.pardir, 'test', testDir)):
                filePath = os.path.join(os.curdir, os.pardir, 'test', testDir, fileName)
                testCalculator = WordFrequencyCalculator()
                testCalculator.train(filePath)
                wfCount = testCalculator.updateWfCount(self.aggregatedWordSet)
                tempFile = open('temp_out.txt', 'w')
                tempFile.writelines("%s %d \n" %(key, value) for key, value in wfCount.iteritems())
                data = wfCount.values()
                fileEstimations[fileName] = data
                prediction = self.svc.predict(data)
                predictedClass = self.trainClassList[prediction]
                filePredictions[fileName] = predictedClass
                if predictedClass == testDir:
                    correctPrediction += 1

            totalFileCount = len(os.listdir(os.path.join(os.curdir, os.pardir, 'test', testDir)))
            testDirAccuracy[testDir] = correctPrediction / totalFileCount * 100.0
            break

        return
