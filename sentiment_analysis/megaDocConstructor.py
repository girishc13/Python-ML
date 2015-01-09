'''
Mega doc constructor for sentiment analysis
'''
import os

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


def constructMegaDocForPos(classDirName):
    posDir = os.path.join(os.curdir, "txt_sentoken", classDirName)
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

    writeMegaDoc(posTrainFoldDict, "mega_train_" + classDirName + "_doc.txt")
    writeMegaDoc(posTestFoldDiict, "mega_test_" + classDirName + "_doc.txt")


if __name__ == "__main__":
    constructMegaDocForPos("pos")
    constructMegaDocForPos("neg")
