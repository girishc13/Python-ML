'''
Trying re.scanner
'''
from blueman.iniparse.ini import lower
from collections import OrderedDict
import os
import re

__author__ = 'girish'


def addTokenToDict(token):
    if token in wFCount:
        wFCount[token] += 1
    else:
        wFCount[token] = 1


def extractWordEndPeriod(token):
    searchEowPeriod = re.search(eowPeriodRegex, token)
    if searchEowPeriod:
        addTokenToDict(searchEowPeriod.string[0:searchEowPeriod.start(2)].lower())
        addTokenToDict('.')
    else:
        addTokenToDict(token.lower())


def extractBracketedWord(token):
    searchBracket = re.search(bracketedWordRegex, token)
    if searchBracket:
        if searchBracket:
            addTokenToDict(searchBracket.group(2).lower())
    else:
        addTokenToDict(token.lower())


if __name__ == '__main__':
    eowPeriodRegex = r'([A-Za-z]{2,})(\.)$'

    bracketedWordRegex = r"(\<)?([A-Za-z\.]+)(\>)?"
    scanner = re.Scanner([
        (r"[0-9]+?\-?\.?[0-9\/]+", lambda scanner, token: ("NUMBER", token)),
        (bracketedWordRegex, lambda scanner, token: ("IDENTIFIER", token)),
        (r"[,.?!-]+", lambda scanner, token: ("PUNCTUATION", token)),
        (r"\s+", None),  # None == skip token.
    ])

    filePath = 'test_text.txt'
    # trainClass = 'acq'
    # filePath = os.path.join(os.curdir, os.pardir, 'train', trainClass, trainClass + '_mega.txt')
    textFile = open(filePath, 'r')
    # line = textFile.readline()
    lineNum = 0
    wFCount = {}
    for line in textFile.readlines():
        results, remainder = scanner.scan(line)
        print results
        lineNum += 1

        for tokType, token in results:
            if tokType == 'IDENTIFIER':
                extractWordEndPeriod(token)
                extractBracketedWord(token)
            else:
                addTokenToDict(token.lower())

    wordCountFile = open('word_count.txt', 'w')
    wordCountFile.writelines(
        "%s \t %d\n" % (key, value) for key, value in OrderedDict(sorted(wFCount.items())).iteritems())
    wordCountFile.close()