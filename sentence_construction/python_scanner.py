'''
Trying re.scanner
'''
import os
import re

__author__ = 'girish'

if __name__ == '__main__':
    scanner = re.Scanner([
        (r"[0-9\.\-\/]+", lambda scanner, token: ("NUMBER", token)),
        (r"(\<)?[A-Za-z\._-]+(\>)?", lambda scanner, token: ("IDENTIFIER", token)),
        (r"[,.?!]+", lambda scanner, token: ("PUNCTUATION", token)),
        (r"\s+", None),  # None == skip token.
    ])

    filePath = 'test_text.txt'
    # trainClass = 'acq'
    # filePath = os.path.join(os.curdir, os.pardir, 'train', trainClass, trainClass + '_mega.txt')
    textFile = open(filePath, 'r')
    # line = textFile.readline()
    lineNum = 0
    for line in textFile.readlines():
        results, remainder = scanner.scan(line)
        print results
        lineNum += 1
        # if lineNum == 10:
            # break
