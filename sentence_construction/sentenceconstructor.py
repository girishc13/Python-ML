__author__ = 'girish'

# Sentence construction trials

# Imports
import re


class SentenceConstructor():
    def construct(self, fileName, excluePunctuations=False):
        sample_text = open(fileName, "r")
        textData = sample_text.read()
        tokenized = re.split(r'\s', textData)

        eowPunct = r'\?|\!\s|\?$|\!$|\,$'
        eowPeriod = r'\.\s|\.$'
        bowApos = r'(\"|\()?([\w]+)(\'|-|\/)?(\))?(\,)?(\")?'
        bowUpper = r'^[A-Z]$|^[A-Z][a-z]+|\"\w+'
        nonWord = r'\W'

        sentences = []
        currSent = []
        tokenIter = iter(tokenized)
        endsWithPeriod = False

        regexPunct = r'\,|\:|\)(\,?\")?$'
        regexEos = r'\?|\!\s|\?\$|\!$|\.\s|\.$'

        try:
            while True:
                token = tokenIter.next()

                if token == '':
                    continue

                # if previous token ended with period then check if the current token starts with
                # Uppercase letter to cut-off the sentence
                if endsWithPeriod:
                    matchUpper = re.search(bowUpper, token)
                    if matchUpper:
                        eosWord = currSent.pop()
                        searchEos = re.search(regexEos, eosWord)
                        currSent.append(searchEos.string[0:searchEos.start(0)].lower())
                        if not excluePunctuations:
                            currSent.append(searchEos.string[searchEos.start(0):searchEos.end(0)].lower())

                        sentences.append(currSent)
                        # print currSent + "\n"
                        currSent = []

                endsWithPeriod = False

                # currSent += token + " "

                # check for ?. ! punctuation
                matchPunct = re.search(eowPunct, token)
                matchPeriod = re.search(eowPeriod, token)
                matchBegApos = re.search(bowApos, token)
                if matchPunct:
                    searchPunct = re.search(regexPunct, token)
                    searchEos = re.search(regexEos, token)
                    if searchPunct:
                        group = searchPunct.group(0)
                        currSent.append(searchPunct.string[0:searchPunct.start(0)].lower())
                        if not excluePunctuations:
                            currSent.append(searchPunct.string[searchPunct.start(0):searchPunct.end(0)].lower())
                    elif searchEos:
                        currSent.append(searchEos.string[0:searchEos.start(0)].lower())
                        if not excluePunctuations:
                            currSent.append(searchEos.string[searchEos.start(0):searchEos.end(0)].lower())
                    else:
                        currSent.append(token.lower())
                elif matchPeriod:
                    currSent.append(token.lower())
                    endsWithPeriod = True
                elif matchBegApos:
                    searchWord = re.search(bowApos, token)
                    if not excluePunctuations and searchWord.group(1):
                        currSent.append(searchWord.group(1).lower())
                    if searchWord.group(2):
                        currSent.append(searchWord.group(2).lower())
                    if not excluePunctuations and searchWord.group(3):
                        currSent.append(searchWord.group(3).lower())
                    if not excluePunctuations and searchWord.group(4):
                        currSent.append(searchWord.group(4).lower())
                    if not excluePunctuations and searchWord.group(5):
                        currSent.append(searchWord.group(5).lower())
                    if not excluePunctuations and searchWord.group(6):
                        currSent.append(searchWord.group(6).lower())
                else:
                    matchNonWord = re.match(nonWord, token)
                    if not matchNonWord:
                        currSent.append(token.lower())

        except StopIteration:
            if currSent:
                if endsWithPeriod:
                    eosWord = currSent.pop()
                    searchEos = re.search(regexEos, eosWord)
                    currSent.append(searchEos.string[0:searchEos.start(0)].lower())
                    if not excluePunctuations:
                        currSent.append(searchEos.string[searchEos.start(0):searchEos.end(0)].lower())
                    sentences.append(currSent)
                else:
                    currSent.append('.')
                    sentences.append(currSent)

        return sentences


