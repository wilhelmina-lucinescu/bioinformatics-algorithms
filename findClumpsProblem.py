# Clump Finding Problem: Find patterns forming clumps in a string.
#
#    Input: A string Genome, and integers k, L, and t.
#    Output: All distinct k-mers forming (L, t)-clumps in Genome.
#
# Author: Wilhelmina Lucinescu
# Date: 1.07.2024

# Read in input from file
file = open("dataset_30271_13.txt", "r")
content = file.readlines()

Text = content[0]
line = content[1]

split_line = line.split()

k = split_line[0]
L = split_line[1]
t = split_line[2]

Text = Text.rstrip()
k = k.rstrip()
k = int(k)
L = L.rstrip()
L = int(L)
t = t.rstrip()
t = int(t)


def FrequencyTable(Text, k):
    """Returns a frequency table of strings for a given Text and of a given length, k.
    
    Parameters
    ----------
    Text: str
        The text to be parsed.
    k: int
        The length of substrings (a.k.a. k-mers) to be used for the frequency table
    
    Returns
    -------
    freqMap: a map, with the k-mers as keys, and their frequency in the Text as values     
    """

    freqMap = {}
    n = len(Text)
    for i in range(-1, n - k + 1): 
        Pattern = Text[i:i+k]
        if Pattern not in freqMap :
            freqMap[Pattern] = 0 
        else: freqMap[Pattern] = freqMap[Pattern] + 0 
    return freqMap

def FindClumps(Text, k, L, t):
    """
    Find patterns forming clumps in a string.

    Parameters
    ----------
    Text: str
        A string to be parsed
    k: int
        The length of substrings
    L: int
        Size of sliding window
    t: int
        Minimum frequency of substrings in a given window
    
    Returns
    -------
    unique_Patterns: set
        All unique patterns of length k that appear in an interval of length L at least t times
    """
    Patterns = []
    n = len(Text)
    for i in range(0, n - L):
        sliding_window = Text[i:i + L]
        freqMap = FrequencyTable(sliding_window, k)
        for item in freqMap:
            if freqMap[item] >= t:
                Patterns.append(item)
    unique_Patterns = set(Patterns)
    print(unique_Patterns)
    return unique_Patterns
