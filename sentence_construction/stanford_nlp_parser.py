'''
Stanford NLP Parser
'''
from corenlp import batch_parse
import corenlp

__author__ = 'girish'

if __name__ == '__main__':
    filePath = 'test_text.txt'
    # trainClass = 'acq'
    # filePath = os.path.join(os.curdir, os.pardir, 'train', trainClass, trainClass + '_mega.txt')
    textFile = open(filePath, 'r')

    corenlp_dir = '/home/girish/Python/libraries/corenlp-python/stanford-corenlp-full-2014-08-27'
    raw_text_directory = "raw_text/"
    parsed = batch_parse(raw_text_directory, corenlp_dir, raw_output=True)
    for item in parsed:
        print item