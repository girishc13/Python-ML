# Parses the training set and calculates the number of words in the vocabulary
# for all classes

# Imports
import sys
import os
import os.path

class VocabularyCalculator():
    
    def __init__(self):
        # count of all the words in the train set
        self.word_count = {}
        # count of the number of words in each class
        self.classVocabCount = {}
        self.vocabCount = 0
        
    
    def calculate(self, dir):
        print "calculating Vocabulary..."
        # iterate through all folders in dir
        self.vocabCount = 0
        for classDir in os.listdir(dir):
            file = None

            filename = classDir + "_" + "mega.txt"

            # init each class count to zero
            self.classVocabCount[classDir] = 0
            #print filename
            file = open(os.path.join(dir, classDir, filename), "r")
            for line in file:
                words = line.split()
                for word in words:
                    word = word.lower()
                    self.classVocabCount[classDir] +=1
                    # if word in present in dict add to the count else
                    # add the word with count 1
                    if word in self.word_count:
                        self.word_count[word] += 1
                    else:
                        self.word_count[word] = 1

            file.close()
        
        for word, count in self.word_count.iteritems():
            self.vocabCount += count
            
        self.word_count = {}
        print "Vocabulary Count: ", self.vocabCount
        return self.vocabCount
    
    def getvocabCount(self):
        return self.vocabCount
    
    def getClassVocabCount(self):
        return self.classVocabCount