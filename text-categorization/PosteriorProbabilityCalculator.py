# Posterior Probability calculator

# Imports
from __future__ import division
import sys
import os
import os.path

class PosteriorProbCalc():

    def calcPosteriorProb(self, dir, priors, condProb):

         cmap = {}

         for classDir in os.listdir(dir):
             file = None
             if classDir == 'grain':
                 filename = classDir + "_" + "mega.txt"

                 file = open(os.path.join(dir, classDir, filename), 'r')

