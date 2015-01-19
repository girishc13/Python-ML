__author__ = 'girish'
# Testing Python regex

import re

sentence = ['I', 'currently', 'reside,', 'in', 'the', 'U.S.A.', 'etc.', 'as', 'a', 'measure.']
# sentence = ['Reuter?']
regexPunct = r'\,|\:'
regexEos = r'\?|\!\s|\?\$|\!$|\.\s|\.$'
regexr = r'\b([a-zA-Z]+)\b|(\d*(\.|,)\d+)|([\d]+\w+)'

for word in sentence[:-1]:
    # regexPunct = r'\,|\:'
    # regexEos = r'\.|\?|\!'
    searchPunct = re.search(regexPunct, word)
    if searchPunct:
        group = searchPunct.group(0)
        # print word, searchRegex.string[searchRegex.start(0):searchRegex.end(0)], searchRegex.start(0),
        # searchRegex.end(0)
        print searchPunct.string[0:searchPunct.start(0)], searchPunct.string[searchPunct.start(0):searchPunct.end(0)]
    else:
        print word

    matchRegexr = re.search(regexr, word)
    if matchRegexr:
        print matchRegexr.group(0)
        print matchRegexr.group(1)
        print matchRegexr.group(2)

eosWord = sentence[len(sentence) - 1]
searchEos = re.search(regexEos, eosWord)
if searchEos:
    print searchEos.string[0:searchEos.start(0)], searchEos.string[searchEos.start(0):searchEos.end(0)]
else:
    print eosWord