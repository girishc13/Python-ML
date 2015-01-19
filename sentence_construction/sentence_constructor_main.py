'''
Main file for testing sentence constructor
'''
from collections import OrderedDict
import os
import collections

__author__ = 'girish'
from sentenceconstructor import SentenceConstructor

if __name__ == '__main__':
    sentConstructor = SentenceConstructor()
    fileName = 'test_text.txt'
    # trainClass = 'acq'
    # fileName = os.path.join(os.curdir, os.pardir, 'train', trainClass, trainClass + '_mega.txt')
    sentences = sentConstructor.construct(fileName, excluePunctuations=True)
    # sentences = sentConstructor.construct(fileName, excluePunctuations=False)

    # reconstructedFile = open('reconstructed_text.txt', 'w')
    # for sentence in sentences:
    # print sentence
    #     reconstructedFile.writelines("%s " % item for item in sentence)
    #     reconstructedFile.writelines("\n")
    # reconstructedFile.close()

    wordCountFile = open('word_count.txt', 'w')
    wFCount = {}
    for sentence in sentences:
        print sentence
        for token in sentence:
            if token in wFCount:
                wFCount[token] += 1
            else:
                wFCount[token] = 1
    wordCountFile.writelines("%s \t %d\n" % (key, value) for key, value in OrderedDict(sorted(wFCount.items())).iteritems())
    wordCountFile.close()