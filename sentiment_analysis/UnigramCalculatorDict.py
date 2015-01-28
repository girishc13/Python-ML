'''
Class to hold sentiment analysis unigram calculators
'''
import operator
import os
from UnigramCalculator import UnigramCalculator

__author__ = 'girish'

class UnigramCalculatorDict(object):
    def initAndTrainClassifier(self, className, fileName):
        posCalculator = UnigramCalculator()
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
        posCalculator = UnigramCalculator()
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
        for classDir in os.listdir(trainDir):
            megaDocPath = os.path.join(trainDir, classDir, 'mega_' + 'train' + '_df_' + classDir + '.txt')
            self.initAndCalculateSvmFeaturesForReuters(classDir, megaDocPath)

        for trainClass, calculator in self.__calculators.items():
            negativeClassFeatureList = []
            for negClass, negCalculator in self.__calculators.items():
                if negClass != trainClass:
                    negativeClassFeatureList.append(
                        negCalculator.calculateWfCountForInputSet(calculator.featureDict.keys()).values())

            calculator.trainBinarySVM(negativeClassFeatureList)

    def initAndCalculateSvmFeaturesForReuters(self, className, megaDocPath):
        posCalculator = UnigramCalculator()
        self.__calculators[className] = posCalculator
        posCalculator.calculateFeatureList(megaDocPath)

    def testWithSVM(self):
        testDir = os.path.join(os.curdir, os.pardir, "test")
        for classDir in os.listdir(testDir):
            megaDocPath = os.path.join(testDir, classDir, 'mega_' + 'test' + '_df_' + classDir + '.txt')
            self.testForFileNameReutersWithSvm(megaDocPath)

    def testForFileNameReutersWithSvm(self, megaDocPath):
        estimations = {}
        testCalculator = UnigramCalculator()
        testCalculator.train(megaDocPath)
        for className, trainCalculator in self.__calculators.iteritems():
            testFeatures = testCalculator.calculateWfCountForInputSet(trainCalculator.featureDict.keys()).values()
            estimations[className] = trainCalculator.testWithSvm(testFeatures)
        predictedClass = max(estimations.iteritems(), key=operator.itemgetter(1))[0]
        print "Predicted class for ", megaDocPath, "is: ", predictedClass