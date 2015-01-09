'''
Main file for spelling correction tasks
'''
from SpellingCorrectionSuggestor import SpellingCorrectionSuggestor

__author__ = 'girish'

if __name__ == "__main__":
    print "Spelling correction task."
    suggestor = SpellingCorrectionSuggestor()
    suggestor.suggest("acress")
    print "Done."
