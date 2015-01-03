__author__ = 'girish'
# Main file for text classification using n-gram model, Good-Turing smoothing and sentence construction

# Imports
import sys
import os
import os.path

if __name__ == "__main__":
    currentDir = os.curdir
    trainDir = os.path.join(currentDir, "../train")
    testDir = os.path.join(currentDir, "../test")

