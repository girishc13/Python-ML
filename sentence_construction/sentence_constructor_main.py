'''
Main file for testing sentence constructor
'''
__author__ = 'girish'
from sentenceconstructor import SentenceConstructor

if __name__ == '__main__':
    sentConstructor = SentenceConstructor()
    # fileName = 'test_text.txt'
    fileName = 'interest_mega.txt'
    # sentences = sentConstructor.construct(fileName, excluePunctuations=True)
    sentences = sentConstructor.construct(fileName, excluePunctuations=False)
    reconstructedFile = open('reconstructed_text.txt', 'w')
    for sentence in sentences:
        print sentence
        reconstructedFile.writelines("%s " % item for item in sentence)
        reconstructedFile.writelines("\n")

