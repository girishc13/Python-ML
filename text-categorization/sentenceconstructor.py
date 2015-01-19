__author__ = 'girish'

# Sentence construction trials

# Imports
import re


class SentenceConstructor():
    def construct(self, fileName, excluePunctuations=False):
        sample_text = open(fileName, "r")
        textData = sample_text.read()
        tokenized = re.split(r'\s', textData)

        eosPunct = r'\?|\!\s|\?\$|\!$|\,$'
        eosPeriod = r'\.\s|\.$'
        bowApos = r'\"\w+'
        startUpper = r'^[A-Z]|\"\w+'
        regexNonWord = r'\W'

        sentences = []
        currSent = []
        tokenIter = iter(tokenized)
        endsWithPeriod = False

        regexPunct = r'\,|\:'
        regexEos = r'\?|\!\s|\?\$|\!$|\.\s|\.$'

        try:
            while True:
                token = tokenIter.next().lower()

                if token == '':
                    continue

                # if previous token ended with period then check if the current token starts with
                # Uppercase letter to cut-off the sentence
                if endsWithPeriod:
                    matchUpper = re.search(startUpper, token)
                    if matchUpper:
                        eosWord = currSent.pop()
                        searchEos = re.search(regexEos, eosWord)
                        currSent.append(searchEos.string[0:searchEos.start(0)])
                        if not excluePunctuations:
                            currSent.append(searchEos.string[searchEos.start(0):searchEos.end(0)])

                        sentences.append(currSent)
                        # print currSent + "\n"
                        currSent = []

                endsWithPeriod = False

                # currSent += token + " "

                # check for ?. ! punctuation
                matchPunct = re.search(eosPunct, token, re.MULTILINE)
                matchPeriod = re.search(eosPeriod, token, re.MULTILINE)
                matchBegApos = re.search(bowApos, token)
                if matchPunct:
                    searchPunct = re.search(regexPunct, token)
                    searchEos = re.search(regexEos, token)
                    if searchPunct:
                        group = searchPunct.group(0)
                        currSent.append(searchPunct.string[0:searchPunct.start(0)])
                        if not excluePunctuations:
                            currSent.append(searchPunct.string[searchPunct.start(0):searchPunct.end(0)])
                    elif searchEos:
                        currSent.append(searchEos.string[0:searchEos.start(0)])
                        if not excluePunctuations:
                            currSent.append(searchEos.string[searchEos.start(0):searchEos.end(0)])
                    else:
                        currSent.append(token)
                elif matchPeriod:
                    currSent.append(token)
                    endsWithPeriod = True
                elif matchBegApos:
                    searchWord = re.search(r'\w+', token)
                    currSent.append(searchWord.group(0))
                else:
                    matchNonWord = re.match(regexNonWord, token)
                    if not matchNonWord:
                        currSent.append(token)

        except StopIteration:
            if currSent:
                sentences.append(currSent)

        return sentences


