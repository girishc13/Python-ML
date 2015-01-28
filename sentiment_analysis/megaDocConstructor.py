'''
Mega doc constructor for sentiment analysis
'''
import os
import re

from nltk import WordPunctTokenizer

from orderedset import OrderedSet


__author__ = 'girish'


def writeFoldDictToFile(megaDoc, foldDict):
    for fold, foldWords in foldDict.items():
        for fileName, wordList in foldWords.items():
            for word in wordList:
                megaDoc.write(word + "\n")


def writeMegaDoc(posTrainFoldDict, fileName):
    megaTrainPosDoc = open(fileName, "w")
    writeFoldDictToFile(megaTrainPosDoc, posTrainFoldDict)
    megaTrainPosDoc.close()


def constructMegaDocForPos(classPath):
    posDir = os.path.join(os.curdir, classPath)
    posFilenameList = sorted(os.listdir(posDir))
    posTrainFoldDict = {}
    posTestFoldDiict = {}
    fold = 0
    fileCounterStartIdx = 0
    fileCounterEndIdx = fileCounterStartIdx + 99
    while fold < 10:
        posTrainFoldDict[fold] = {}
        posTestFoldDiict[fold] = {}
        for fileIndex in range(fileCounterStartIdx, fileCounterEndIdx):
            fileName = posFilenameList[fileIndex]
            textData = open(os.path.join(posDir, fileName)).read()
            sentences = textData.split()
            posTrainFoldDict[fold][fileName] = OrderedSet(sentences)

        fileName = posFilenameList[fileCounterEndIdx]
        textData = open(os.path.join(posDir, fileName)).read()
        sentences = textData.split()
        posTestFoldDiict[fold][fileName] = OrderedSet(sentences)

        fold += 1
        fileCounterStartIdx = fileCounterEndIdx + 1
        fileCounterEndIdx += 99 + 1

    writeMegaDoc(posTrainFoldDict, "mega_train_" + classPath + "_doc.txt")
    writeMegaDoc(posTestFoldDiict, "mega_test_" + classPath + "_doc.txt")


def constructMegaDocForDir(dataSetDir, dataSetType):
    for classDir in os.listdir(dataSetDir):
        rawData = open(
            os.path.join(os.path.curdir, os.path.pardir, dataSetType, classDir, classDir + '_mega.txt'),
            'r').read()
        tokenSet = []
        punctRegex = r'[-\.<>,\/0-9$!\'\"\(\)&*:;^\[\]]'
        tokenizer = WordPunctTokenizer()
        tokenList = tokenizer.tokenize(rawData)
        for token in tokenList:
            matchPunct = re.search(punctRegex, token)
            if not matchPunct and token != '\x03':
                tokenSet.append(token.lower())

        megaDoc = open(os.path.join(dataSetDir, classDir, 'mega_' + dataSetType + '_df_' + classDir + '.txt'), 'w')
        for token in tokenSet:
            megaDoc.write(token + '\n')

        megaDoc.close()


def constructMegaDocForReuters():
    trainDir = os.path.join(os.curdir, os.pardir, "train")
    constructMegaDocForDir(trainDir, "train")

    testDir = os.path.join(os.curdir, os.pardir, "test")
    constructMegaDocForDir(testDir, "test")


if __name__ == "__main__":
    # constructMegaDocForPos("txt_sentoken" + "pos")
    # constructMegaDocForPos("txt_sentoken" + "neg")


    constructMegaDocForReuters()