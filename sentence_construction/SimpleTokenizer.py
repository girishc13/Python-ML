'''
Simple tokenizer based on white space and punctuations
'''
import re

__author__ = 'girish'


class SimpleTokenizer(object):
    def __init__(self):
        self.eowRegex = r'(>)?(\.)(\"|\')?$|(\?|\!)$'
        self.eowDelims = ['.', '?', '!']
        self.begSentRegex = r'(^[A-Z]$)|(^[A-Z][a-z]+)|(\"\w+)'
        self.wordPunctRegex = r'(\")?(\<)?(\()?([\w\/\-]+)(\))?(\,)?(\")?(\>)?'

    def extractAndAppendEow(self, token, searchRegex):
        searchEow = re.search(searchRegex, token)
        if not searchEow:
            self.curSent.append(token)
        if not self.exclPunct and searchEow:
            for group_num in range(1, self.num_groups(searchRegex) + 1):
                if searchEow.group(group_num):
                    # self.curSent.append(searchEow.group(group_num))
                    self.extractAndAppendPunctuatedWord(searchEow.group(group_num))

    def terminateCurSent(self, token):
        self.extractAndAppendEow(token, self.eowRegex)
        self.sentences.append(self.curSent)
        self.curSent = []

    def handleOnBoundary(self, token):
        matchEow = re.search(self.eowRegex, token)
        if matchEow:
            if matchEow.group(1):
                self.endsWithPeriod = True
                self.extractAndAppendPunctuatedWord(token)
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
                if self.endsWithPeriod and token == '':
                    self.terminateCurSent(self.curSent.pop())
                    self.endsWithPeriod = False
                    continue
                elif self.endsWithPeriod:
                    matchBegSent = re.search(self.begSentRegex, token)
                    if matchBegSent and (matchBegSent.group(1) or matchBegSent.group(2) or matchBegSent.group(3)):
                        self.terminateCurSent(self.curSent.pop())
                    self.endsWithPeriod = False

                if not self.handleOnBoundary(token):
                    self.extractAndAppendPunctuatedWord(token)

        except StopIteration:
            if self.curSent:
                eosWord = self.curSent.pop()
                if eosWord != '':
                    self.terminateCurSent(eosWord)

        return self.sentences

    def num_groups(self, regex):
        return re.compile(regex).groups

    def extractAndAppendPunctuatedWord(self, token):
        matchPunctsAndWord = re.search(self.wordPunctRegex, token)
        if matchPunctsAndWord:
            for group_num in range(1, self.num_groups(self.wordPunctRegex) + 1):
                if group_num == 4:
                    self.curSent.append(matchPunctsAndWord.group(group_num).lower())
                elif not self.exclPunct and matchPunctsAndWord.group(group_num):
                    self.curSent.append(matchPunctsAndWord.group(group_num).lower())
        else:
            self.curSent.append(token)