'''
Simple tokenizer based on white space and punctuations
'''
import re

__author__ = 'girish'


class SimpleTokenizer(object):
    def __init__(self):
        self.eowRegex = r'(\.)|(\?|\!)'
        self.eowDelims = ['.', '?', '!']
        self.begSentRegex = r'(^[A-Z]$)|(^[A-Z][a-z]+)|(\"\w+)'

    def extractAndAppendEow(self, token, searchRegex):
        searchEow = re.search(searchRegex, token)
        self.curSent.append(searchEow.string[0:searchEow.start(0)].lower())
        if not self.exclPunct:
            self.curSent.append(searchEow.string[searchEow.start(0):searchEow.end(0)].lower())

    def terminateCurSent(self, token):
        self.extractAndAppendEow(token, self.eowRegex)
        self.sentences.append(self.curSent)
        self.curSent = []

    def handleIfBoundary(self, token):
        matchEow = re.search(self.eowRegex, token)
        if matchEow:
            if matchEow.group(1):
                self.endsWithPeriod = True
                self.curSent.append(token)
            else:
                self.terminateCurSent(token)
            return True

    def tokenize(self, filePath, excludePunctuations=False):
        self.exclPunct = excludePunctuations
        textData = open(filePath, 'r').read()
        tokenized = re.split(r'\s', textData)

        self.sentences = []
        self.curSent = []
        boundarySeen = False
        self.endsWithPeriod = False
        tokenIter = iter(tokenized)

        try:
            while True:
                token = tokenIter.next()

                # modify last word to terminate or continue the current sentence
                if self.endsWithPeriod:
                    matchBegSent = re.search(self.begSentRegex, token)
                    if matchBegSent and (matchBegSent.group(1) or matchBegSent.group(2) or matchBegSent.group(3)):
                        eosWord = self.curSent.pop()
                        self.terminateCurSent(eosWord)
                    self.endsWithPeriod = False

                if not self.handleIfBoundary(token):
                    self.curSent.append(token)

        except StopIteration:
            if self.curSent:
                self.sentences.append(self.curSent)

        return self.sentences
