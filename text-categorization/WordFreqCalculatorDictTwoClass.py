'''
Class for performing two-class text categorization
'''
import os

from WordFrequencyCalculator import WordFrequencyCalculator


__author__ = 'girish'


class WordFreqCalculatorDictTwoClass(object):
    def calculateClassWordFrequencies(self):
        for trainDir in os.listdir(os.path.join(os.curdir, os.pardir, 'train')):
            calculator = WordFrequencyCalculator()
            self.__calculators[trainDir] = calculator
            filePath = os.path.join(os.curdir, os.pardir, 'train', trainDir, trainDir + '_mega.txt')
            calculator.calculateWordFreqs(filePath)

    def train(self):
        self.__calculators = {}
        self.calculateClassWordFrequencies()
        for trainClass, calculator in self.__calculators.items():
            # negativeClassFeatureList = [negCalc.featureDict.values() for trainClasses, negCalc in
            # self.calculators.items() if

            # trainClasses != trainClass]

            negativeClassFeatureList = []
            for negClass, negCalculator in self.__calculators.items():
                if negClass != trainClass:
                    negativeClassFeatureList.append(
                        negCalculator.calculateWfCountForInputSet(calculator.featureDict.keys()).values())

            calculator.trainBinarySVM(negativeClassFeatureList)

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
                testCalculator.calculateWordFreqs(filePath)

                predictions = {}
                for trainClass, trainCalculator in self.__calculators.items():
                    testFeatures = testCalculator.calculateWfCountForInputSet(trainCalculator.featureDict.keys()).values()
                    predictions[trainClass] = trainCalculator.predict(testFeatures)

                break

        return
