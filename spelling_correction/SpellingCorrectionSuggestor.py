'''
Suggessts a list of corrections for the misspelled word
'''
import os

from UnigramCalculator import UnigramCalculator


__author__ = 'girish'


class SpellingCorrectionSuggestor(object):
    def buildTrainDirectory(self):
        currentDir = os.curdir
        trainDir = os.path.abspath(os.path.join(currentDir, os.pardir, "train"))
        return trainDir

    def suggest(self, misspelledWord):
        unigramCalculator = UnigramCalculator()
        unigramCalculator.calculate(self.buildTrainDirectory())
        candidateList = unigramCalculator.getCandidateList(misspelledWord)
        print candidateList
        edits = self.edits1(misspelledWord, candidateList)

    def edits1(self, word, candidateList):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word, candidateList[i]) for i in range(len(candidateList))]
        deletes = [a + b[1:] for a, b in splits if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
        replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
        inserts = [a + c + b for a, b in splits for c in alphabet]
        return set(deletes + transposes + replaces + inserts)