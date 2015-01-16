'''
Feature value calculator for a single file/class
'''
import os
import re

__author__ = 'girish'


class FeatureCalculator(object):
    def fetchRawData(self, classDir):
        textFile = open(os.path.join(os.curdir, classDir, classDir + '_' + 'mega.txt'), 'r')
        return textFile.read()

    def fetchSentences(self, classDir):
        data = self.fetchRawData(classDir)
        return re.split(r'( *[\.])', data)

    def train(self, classDir):
        sentences = self.fetchSentences(classDir)
        for sentence in sentences:
            for token in sentence.split():
                break
