from types import NoneType
__author__ = 'girish'

# Sentence construction trials

# Imports
import re

class SentenceConstructor():

    def construct(self, filePath):
        sample_text = open(filePath, "r")
        textData = sample_text.read()
        tokenized = re.split(r'\s',textData)

        eosPunct = r'\?|\!\s|\?\$|\!$|\,$'
        eosPeriod = r'\.\s|\.$'
        startUpper = r'^[A-Z]'

        sentences = []
        currSent = []
        tokenIter = iter(tokenized)
        endsWithPeriod = False

        regexPunct = r'\,|\:'
        regexEos = r'\?|\!\s|\?\$|\!$|\.\s|\.$'

        try:
            while True:
                token = tokenIter.next()

                if token == '':
                    continue

                # if previous token ended with period then check if the current token starts with
                # Uppercase letter to cut-off the sentence
                if endsWithPeriod:
                    matchUpper = re.search(startUpper, token)
                    if matchUpper:
                        eosWord = currSent.pop()
                        searchEos = re.search(regexEos, eosWord)
                        if searchEos is None:
                            currSent.append(".")
                        else:
                            currSent.append(searchEos.string[0:searchEos.start(0)])
                            currSent.append(searchEos.string[searchEos.start(0):searchEos.end(0)])

                        sentences.append(currSent)
                        # print currSent + "\n"
                        currSent = []
                        endsWithPeriod = False

                # currSent += token + " "

                # check for ?. ! punctuation
                matchPunct = re.search(eosPunct, token, re.MULTILINE)
                matchPeriod = re.search(eosPeriod, token, re.MULTILINE)
                if  matchPunct:
                    searchPunct = re.search(regexPunct, token)
                    searchEos = re.search(regexEos, token)
                    if searchPunct:
                        # print searchPunct.string[0:searchPunct.start(0)], searchPunct.string[searchPunct.start(0):searchPunct.end(0)]
                        currSent.append(searchPunct.string[0:searchPunct.start(0)])
                        currSent.append(searchPunct.string[searchPunct.start(0):searchPunct.end(0)])
                    elif searchEos:
                        currSent.append(searchEos.string[0:searchEos.start(0)])
                        currSent.append(searchEos.string[searchEos.start(0):searchEos.end(0)])
                    else:
                        # print word
                        currSent.append(token)

                    # sentences.append(currSent)
                    # print currSent + "\n"
                    # currSent = []
                elif matchPeriod:
                    currSent.append(token)
                    endsWithPeriod = True
                else:
                    currSent.append(token)

        except StopIteration:
            if currSent:
                sentences.append(currSent)
            # pass
            # print currSent

        return sentences


