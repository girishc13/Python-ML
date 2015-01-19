'''
Testing regex to extract valid tokens from data
'''
import re

__author__ = 'girish'

if __name__ == "__main__":
    textFile = open('sample_text1.txt', 'r')
    rawData = textFile.read()
    regexr = r'\b([a-zA-Z]+)\b|(\d*(\.|,)\d+)|([\d]+\w+)'
    # for token in rawData.split():
    # matchRegexr = re.search(regexr, token)
    matchRegexr = re.findall(regexr, rawData)
    print matchRegexr
    # if matchRegexr:
    #     if matchRegexr.group(0):
    #         print matchRegexr.group(0)
    #     elif matchRegexr.group(0):
    #         print matchRegexr.group(1)
    #     else:
    #         print matchRegexr.group(2)


