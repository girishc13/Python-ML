__author__ = 'girish'
# Main program for calculating trigram model

from unigramMLE import UnigramMLE
from bigramMLE import BigramMLE
from trigramMLE import TrigramMLE

if __name__ == "__main__":
    print "Executing main program..."
    textFileName = "sampleText.txt"
    testFileName = "testText.txt"
    # unigram calculatiorns
    unigramCalc = UnigramMLE(textFileName)
    unigramCalc.calculate()

    # bigram calculations
    bigramCalc = BigramMLE(textFileName)
    bigramCalc.calculate(unigramCalc.getUnigramCount())
    # estimating probability of test text
    bigramCalc.estimateProbability(testFileName)
    # predict next word
    # bigramCalc.predict("Inc")

    # trigram calculations
    trigramCalc = TrigramMLE(textFileName)
    trigramCalc.calculate(bigramCalc.getBigramEst())
    # estimating probability of test text
    trigramCalc.estimateProbability(testFileName)
    # predict next word
    # trigramCalc.predict(("the", "for"))


    user_input = ''

    while 1:
        user_input = raw_input("Enter two words or 'quit' to exit: ")

        if user_input == 'quit':
            break

        inputList = user_input.split()
        inputTuple = (inputList[1], inputList[0])
        # print inputTuple
        trigramCalc.predict(inputTuple)