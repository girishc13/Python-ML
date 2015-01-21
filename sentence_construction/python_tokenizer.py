'''
Trying python tokenizer
'''
from collections import OrderedDict
import os
from tokenize import generate_tokens
from StringIO import StringIO

__author__ = 'girish'

if __name__ == '__main__':
    trainClass = 'acq'
    filePath = os.path.join(os.curdir, os.pardir, 'train', trainClass, trainClass + '_mega.txt')
    textFile = open(filePath, 'r')
    line = textFile.read()
    g = generate_tokens(StringIO(line).readline)

    # try:
    #     for toknum, tokval, _, _, _ in g:
    #         print tokval
    # except:
    #     pass

    wordCountFile = open('word_count.txt', 'w')
    wFCount = {}
    try:
        for toknum, tokval, _, _, _ in g:
            if tokval in wFCount:
                wFCount[tokval] += 1
            else:
                wFCount[tokval] = 1
    except:
        pass

    wordCountFile.writelines(
        "%s \t %d\n" % (key, value) for key, value in OrderedDict(sorted(wFCount.items())).iteritems())
    wordCountFile.close()


