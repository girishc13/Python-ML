'''
Verifying nltk tokenizer
'''
import os
import re
from nltk import TreebankWordTokenizer, OrderedDict, word_tokenize, WordPunctTokenizer

__author__ = 'girish'

if __name__ == '__main__':
    # filePath = 'test_text.txt'
    trainClass = 'acq'
    filePath = os.path.join(os.curdir, os.pardir, 'train', trainClass, trainClass + '_mega.txt')
    textFile = open(filePath, 'r')

    # tokenizer = TreebankWordTokenizer()
    # tokenList = tokenizer.tokenize(textFile.read())

    # tokenList = word_tokenize('Hello World.')

    tokenizer = WordPunctTokenizer()
    tokenList = tokenizer.tokenize(textFile.read())

    # print tokenList
    wordCountFile = open('word_count.txt', 'w')
    wFCount = {}
    punctRegex = r'[-\.<>,\/0-9]'
    for token in tokenList:
        matchPunct = re.search(punctRegex, token)
        if not matchPunct:
            print token
            if token in wFCount:
                wFCount[token] += 1
            else:
                wFCount[token] = 1
    wordCountFile.writelines(
        "%s \t %d\n" % (key, value) for key, value in OrderedDict(sorted(wFCount.items())).iteritems())
    wordCountFile.close()