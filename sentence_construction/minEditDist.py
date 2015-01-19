__author__ = 'girish'
# Algorithm to calculate the min edit distance

# Imports
import numpy as np


def calc():
    # Initialize strings
    X = "a cat"
    lenX = len(X)
    Y = "an act"
    lenY = len(Y)

    # Initialize D
    D = np.zeros((lenX + 1, lenY + 1), dtype=np.int)
    D[0:lenX+1,0] = np.arange(0, lenX+1)
    D[0,0:lenY+1] = np.arange(0, lenY+1)
    # print D

    for i in range(1, lenX + 1):
        for j in range(1, lenY + 1):
            insertD = D[i-1][j] + 1
            deleteD = D[i][j-1] + 1

            subD = D[i-1][j-1]
            if X[i-1] != Y[j-1]:
                subD += 2

            D[i][j] = min(insertD, deleteD, subD)

    print D


    print "Min edit distance: " , D[lenX][lenY]


def calcNW():
    # Initialize strings
    X = "PIECES"
    lenX = len(X)
    Y = "NIECES"
    lenY = len(Y)

    # Initialize D
    D = np.zeros((lenX + 1, lenY + 1), dtype=np.int)
    D[0:lenX+1,0] = np.arange(0, -(lenX+1), -1)
    D[0,0:lenY+1] = np.arange(0, -(lenY+1), -1)
    # print D

    for i in range(1, lenX + 1):
        for j in range(1, lenY + 1):
            insertD = D[i-1][j] - 1
            deleteD = D[i][j-1] - 1

            subD = D[i-1][j-1]
            if X[i-1] != Y[j-1]:
                subD -= 2

            D[i][j] = max(insertD, deleteD, subD)

    print D


    print "Max edit distance: " , D[lenX][lenY]

def optimalStringAlignment():
    # Initialize strings
    X = "pieces"
    lenX = len(X)
    Y = "neice"
    lenY = len(Y)

    # Initialize D
    D = np.zeros((lenX + 1, lenY + 1), dtype=np.int)
    D[0:lenX+1,0] = np.arange(0, lenX + 1)
    D[0,0:lenY+1] = np.arange(0, lenY + 1)
    print D

    for i in range(1, lenX + 1 ):
        for j in range(1, lenY + 1):
            cost = 0
            if X[i-1] != Y[j-1]:
                cost = 1

            insertD = D[i-1][j] + 1
            deleteD = D[i][j -1] + 1
            subD = D[i-1][j-1] + cost

            D[i][j] = min(insertD, deleteD, subD)

            if i > 1 and j > 1 and X[i-1] == Y[j-2] and X[i-2] == Y[j-1]:
                D[i][j] = min(D[i][j], D[i-2][j-2] + 1)

    print D
    print "Min edit distance: " , D[lenX][lenY]

def damerau_levenshtein_distance(a, b):
    # "Infinity" -- greater than maximum possible edit distance
    # Used to prevent transpositions for first characters
    INF = len(a) + len(b)

    # Matrix: (M + 2) x (N + 2)
    matrix  = [[INF for n in xrange(len(b) + 2)]]
    matrix += [[INF] + range(len(b) + 1)]
    matrix += [[INF, m] + [0] * len(b) for m in xrange(1, len(a) + 1)]

    # Holds last row each element was encountered: `DA` in the Wikipedia pseudocode
    last_row = {}

    # Fill in costs
    for row in xrange(1, len(a) + 1):
        # Current character in `a`
        ch_a = a[row-1]

        # Column of last match on this row: `DB` in pseudocode
        last_match_col = 0

        for col in xrange(1, len(b) + 1):
            # Current character in `b`
            ch_b = b[col-1]

            # Last row with matching character; `i1` in pseudocode
            last_matching_row = last_row.get(ch_b, 0)

            # Cost of substitution
            cost = 0 if ch_a == ch_b else 1

            # Compute substring distance
            matrix[row+1][col+1] = min(
                matrix[row][col] + cost, # Substitution
                matrix[row+1][col] + 1,  # Addition
                matrix[row][col+1] + 1,  # Deletion

                # Transposition
                matrix[last_matching_row][last_match_col]
                    + (row - last_matching_row - 1) + 1
                    + (col - last_match_col - 1))

            # If there was a match, update last_match_col
            # Doing this here lets me be rid of the `j1` variable from the original pseudocode
            if cost == 0:
                last_match_col = col

        # Update last row for current character
        last_row[ch_a] = row

    # Return last element
    print matrix[-1][-1]

if __name__ == "__main__":
    # calc()
    # calcNW()
    # optimalStringAlignment()
    damerau_levenshtein_distance("pieces", "neice")