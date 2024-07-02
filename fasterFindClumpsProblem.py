#  Clump Finding Problem: Find patterns forming clumps in a string.
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
    for i in range(0, n - k + 1): 
        Pattern = Text[i:i+k]
        if Pattern not in freqMap :
            freqMap[Pattern] = 1 
        else: freqMap[Pattern] = freqMap[Pattern] + 1 
    return freqMap

def fasterFindClumps(Text: str, k: int, L: int, t: int):
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
    sliding_window = Text[0:L]
    freqMap = FrequencyTable(sliding_window, k)
    for key in freqMap:
        if freqMap[key] >= t:
            Patterns.append(key)

    for i in range(1, n - L + 1):
        old = Text[i-1:i+k-1]
        if freqMap[old] > 1 :
            freqMap[old] -= 1
        else: freqMap.pop(old)
        new = Text[L-k+i-1:L+i-1]
        if new in freqMap:
            freqMap[new] += 1
        else:
            freqMap[new] = 1
        if freqMap[new] >= t :
            Patterns.append(new)
    unique_Patterns = set(Patterns)
    return unique_Patterns

clumps = fasterFindClumps(Text, k, L, t)
print(*clumps, sep=' ')
