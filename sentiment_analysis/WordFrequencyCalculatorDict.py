from __future__ import division
from orderedset import OrderedSet

'''
Class to hold sentiment analysis unigram calculators
'''
import operator
import os
from sklearn import svm
from WordFrequencyCalculator import WordFrequencyCalculator

__author__ = 'girish'

class WordFrequencyCalculatorDict(object):
    def initAndTrainClassifier(self, className, fileName):
        posCalculator = WordFrequencyCalculator()
        self.__calculators[className] = posCalculator
        filePath = os.path.join(os.curdir, fileName)
        posCalculator.train(filePath)

    def trainNaiveBayes(self):
        self.__calculators = {}
        # self.initAndTrainClassifier("pos", "mega_train_pos_doc.txt")
        # self.initAndTrainClassifier("neg", "mega_train_neg_doc.txt")

        trainDir = os.path.join(os.curdir, os.pardir, "train")
        for classDir in os.listdir(trainDir):
            megaDocPath = os.path.join(trainDir, classDir, 'mega_' + 'train' + '_df_' + classDir + '.txt')
            self.initAndTrainNaiveBayesClassifierForReuters(classDir, megaDocPath)

    def testForFileNameWithNaiveBayes(self, testFileName):
        estimations = {}
        for className, calculator in self.__calculators.iteritems():
            estimations[className] = calculator.test(testFileName)
        predictedClass = max(estimations.iteritems(), key=operator.itemgetter(1))[0]
        print "Predicted class for ", testFileName, "is: ", predictedClass

    def testWithNaiveBayes(self):
        # self.testForFileName("mega_test_pos_doc.txt")
        # self.testForFileName("mega_test_neg_doc.txt")

        testDir = os.path.join(os.curdir, os.pardir, "test")
        for classDir in os.listdir(testDir):
            megaDocPath = os.path.join(testDir, classDir, 'mega_' + 'test' + '_df_' + classDir + '.txt')
            self.testForFileNameReutersWithNaiveBayes(megaDocPath)

    def initAndTrainNaiveBayesClassifierForReuters(self, className, megaDocPath):
        posCalculator = WordFrequencyCalculator()
        self.__calculators[className] = posCalculator
        posCalculator.train(megaDocPath)

    def testForFileNameReutersWithNaiveBayes(self, megaDocPath):
        estimations = {}
        for className, calculator in self.__calculators.iteritems():
            estimations[className] = calculator.test(megaDocPath)
        predictedClass = max(estimations.iteritems(), key=operator.itemgetter(1))[0]
        print "Predicted class for ", megaDocPath, "is: ", predictedClass

    def trainWithSVM(self):
        self.__calculators = {}
        trainDir = os.path.join(os.curdir, os.pardir, "train")
        wordSet = set()
        for classDir in os.listdir(trainDir):
            megaDocPath = os.path.join(trainDir, classDir, 'mega_' + 'train' + '_df_' + classDir + '.txt')
            self.initAndCalculateSvmFeaturesForReuters(classDir, megaDocPath)
            wordSet.update(self.__calculators[classDir].featureDict)

        self.__aggregatedWordSet = OrderedSet(wordSet)

        # for trainClass, calculator in self.__calculators.items():
        #     negativeClassFeatureList = []
        #     for negClass, negCalculator in self.__calculators.items():
        #         if negClass != trainClass:
        #             negativeClassFeatureList.append(
        #                 negCalculator.calculateWfCountForInputSet(calculator.featureDict.keys()).values())
        #
        #     calculator.trainBinarySVM(negativeClassFeatureList)

        for classDir in os.listdir(trainDir):
            self.__calculators[classDir].calculateWfCountForInputSet(self.__aggregatedWordSet)

        self.__trainClassList = self.__calculators.keys()
        self.__target = [i for i in range(0, len(self.__trainClassList))]

        self.__data = [self.__calculators[key].wfCountAgg.values() for key in  self.__trainClassList]
        self.__norm_data = []
        for featureData in self.__data:
            maxVal = max(featureData)
            minVal = min(featureData)
            norm_feature = [(val - minVal) / (maxVal - minVal) for val in featureData]
            self.__norm_data.append(norm_feature)

        self.__svc = svm.SVC()
        self.__svc.fit(self.__norm_data, self.__target)

        test_predict1 = self.__svc.predict(self.__norm_data[0])
        test_predict2 = self.__svc.predict(self.__norm_data[5])

        return


    def initAndCalculateSvmFeaturesForReuters(self, className, megaDocPath):
        posCalculator = WordFrequencyCalculator()
        self.__calculators[className] = posCalculator
        posCalculator.calculateFeatureList(megaDocPath)

    def testWithSVM(self):
        # testDir = os.path.join(os.curdir, os.pardir, "test")
        # for classDir in os.listdir(testDir):
        #     megaDocPath = os.path.join(testDir, classDir, 'mega_' + 'test' + '_df_' + classDir + '.txt')
        #     self.testForFileNameReutersWithSvm(megaDocPath)

        # testDirEstimation = {}
        # for classDir in os.listdir(testDir):
        #     megaDocPath = os.path.join(testDir, classDir, 'mega_' + 'test' + '_df_' + classDir + '.txt')
        #     testCalculator = UnigramCalculator()
        #     testCalculator.calculateFeatureList(megaDocPath)
        #     testCalculator.calculateWfCountForInputSet(self.__aggregatedWordSet)
        #
        #     test_data = testCalculator.wfCountAgg.values()
        #     maxVal = max(test_data)
        #     minVal = min(test_data)
        #     norm_test_data = [(val - minVal) / (maxVal - minVal) for val in test_data]
        #
        #     prediction = self.__svc.predict(norm_test_data)
        #     predictedClass = self.__trainClassList[prediction]
        #     testDirEstimation[classDir] = predictedClass
        #     continue

        testDirEstimations = {}
        testDirPredictions = {}
        testDirAccuracy = {}
        orderedTestDir = OrderedSet(os.listdir(os.path.join(os.curdir, os.pardir, 'test')))
        for testDir in orderedTestDir:
            fileEstimations = {}
            testDirEstimations[testDir] = fileEstimations
            filePredictions = {}
            testDirPredictions[testDir] = filePredictions
            correctPrediction = 0.0
            totalFileCount = 0.0

            if testDir == 'acq':
                pass

            for fileName in os.listdir(os.path.join(os.curdir, os.pardir, 'test', testDir)):
                filePath = os.path.join(os.curdir, os.pardir, 'test', testDir, fileName)
                testCalculator = WordFrequencyCalculator()
                testCalculator.calculateFeatureList(filePath)
                testCalculator.calculateWfCountForInputSet(self.__aggregatedWordSet)
                # tempFile = open('temp_out.txt', 'w')
                # tempFile.writelines("%s %d \n" %(key, value) for key, value in wfCount.iteritems())

                test_data = testCalculator.wfCountAgg.values()
                maxVal = max(test_data)
                minVal = min(test_data)
                if maxVal == 0:
                    break
                norm_test_data = [(val - minVal) / (maxVal - minVal) for val in test_data]

                fileEstimations[fileName] = norm_test_data
                prediction = self.__svc.predict(norm_test_data)
                predictedClass = self.__trainClassList[prediction]
                filePredictions[fileName] = predictedClass
                totalFileCount += 1
                if predictedClass == testDir:
                    correctPrediction += 1

            # totalFileCount = len(os.listdir(os.path.join(os.curdir, os.pardir, 'test', testDir)))
            if totalFileCount == 0.0:
                testDirAccuracy[testDir] = 0.0
            else:
                testDirAccuracy[testDir] = correctPrediction / totalFileCount * 100.0

        for testDir in testDirAccuracy:
            print "Test class accuracy: ", testDirAccuracy[testDir], "for test class: ", testDir
        return

    def testForFileNameReutersWithSvm(self, megaDocPath):
        estimations = {}
        testCalculator = WordFrequencyCalculator()
        testCalculator.train(megaDocPath)
        for className, trainCalculator in self.__calculators.iteritems():
            testFeatures = testCalculator.calculateWfCountForInputSet(trainCalculator.featureDict.keys()).values()
            prediction = trainCalculator.testWithSvm(testFeatures)
            estimations[className] = prediction
        predictedClass = max(estimations.iteritems(), key=operator.itemgetter(1))[0]
        print "Predicted class for ", megaDocPath, "is: ", predictedClass