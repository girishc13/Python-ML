'''
Main file for testing tokenization
'''
from collections import OrderedDict
import os

from SimpleTokenizer import SimpleTokenizer

__author__ = 'girish'

if __name__ == '__main__':
    tokenizer = SimpleTokenizer()
    # filePath = 'test_text.txt'
    trainClass = 'acq'
    filePath = os.path.join(os.curdir, os.pardir, 'train', trainClass, trainClass + '_mega.txt')
    sentences = tokenizer.tokenize(filePath)

    wordCountFile = open('word_count.txt', 'w')
    wFCount = {}
    for sentence in sentences:
        print sentence
        for token in sentence:
            if token in wFCount:
                wFCount[token] += 1
            else:
                wFCount[token] = 1
    wordCountFile.writelines(
        "%s \t %d\n" % (key, value) for key, value in OrderedDict(sorted(wFCount.items())).iteritems())
    wordCountFile.close()
