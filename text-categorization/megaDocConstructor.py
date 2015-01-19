# Construct mega document for each class

# Imports
import sys
import os
import os.path

# Takes in the path of the folder containing the text files and create a mega
# text document of all the files
class MegaDocumentConstructor():
    
    def process(self, classDir):

        megaFileName = os.path.basename(classDir) + "_mega" + ".txt"
        megaFilePath = os.path.join(classDir, megaFileName)
        megaFile = open(megaFilePath, "w")
        
        for filename in os.listdir(classDir):
            filePath = os.path.join(classDir, filename)
            file = open(filePath, "r")
            data = file.read()            
            megaFile.write(data)
            megaFile.write("\n")
        
        megaFile.close()
    
    


# Main Program    
if __name__ == '__main__':
    
    currentDir = os.curdir
    trainDir = os.path.join(currentDir, os.pardir, "train")
    docConstrucotr = MegaDocumentConstructor()
    
    for classDirName in os.listdir(trainDir):
        classDir = os.path.join(trainDir, classDirName)
        docConstrucotr.process(classDir)
        
    testDir = os.path.join(currentDir, os.pardir, "test")
    for classDirName in os.listdir(testDir):
        classDir = os.path.join(testDir, classDirName)
        docConstrucotr.process(classDir)